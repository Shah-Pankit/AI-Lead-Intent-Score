from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import joblib
import pandas as pd
from reranker import rerank_score
from fastapi.middleware.cors import CORSMiddleware
import logging
import os

# ✅ Correctly load model from root directory
model_path = os.path.join(os.path.dirname(__file__), "..", "lead_intent_model.pkl")
model = joblib.load(model_path)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

leads = []

class Lead(BaseModel):
    Email: EmailStr
    CreditScore: int
    AgeGroup: str
    FamilyBackground: str
    Income: int
    Profession: str
    CompanyType: str
    City: str
    Comment: str
    Consent: bool

@app.post("/score")
async def score_lead(lead: Lead):
    try:
        if not lead.Consent:
            raise HTTPException(status_code=403, detail="Consent is required.")

        input_data = [[
            lead.CreditScore,
            lead.AgeGroup,
            lead.FamilyBackground,
            lead.Income,
            lead.Profession,
            lead.CompanyType,
            lead.City
        ]]

        columns = ["CreditScore", "AgeGroup", "FamilyBackground", "Income", "Profession", "CompanyType", "City"]
        X_dict = {k: [v] for k, v in zip(columns, input_data[0])}
        X_df = pd.DataFrame(X_dict)

        score = model.predict_proba(X_df)[0][1] * 100
        reranked_score = rerank_score(score, lead.Comment)

        leads.append({
            "email": lead.Email,
            "credit_score": lead.CreditScore,
            "income": lead.Income,
            "initial_score": round(score, 2),
            "reranked_score": round(reranked_score, 2),
            "comment": lead.Comment
        })

        return {
            "initial_score": round(score, 2),
            "reranked_score": round(reranked_score, 2)
        }
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/leads")
def get_leads():
    return leads
