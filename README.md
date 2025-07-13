🧠 AI Lead Scoring Dashboard
An AI-powered Lead Scoring Dashboard that predicts customer intent using a machine learning model and adjusts scores via a rule-based LLM-inspired reranker — enabling businesses to prioritize high-quality leads efficiently.

📌 Features
🔮 Predicts intent score (0–100) using a trained ML model
🧠 LLM-based reranker boosts/drops scores based on lead comments
⚡ FastAPI backend with JSON API (/score, /leads)
🌐 Frontend with form + live scoring table (pure HTML, CSS, JS)
📊 Uses a synthetic or sourced dataset with real-world relationships
🏗️ Architecture
[ User Form ] ↓ [ Frontend (JS Form) ] ↓ POST [ FastAPI Backend ] ├── ML Model → Initial Score └──LLM Reranker → Final Score ↓ [ JSON Response → Table Update ]

🧪 How to Run Locally
1. Clone the Repo
git clone https://github.com/your-username/lead-scoring-app.git
cd lead-scoring-app



## 🚀 Backend (FastAPI)

cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload

Visit: http://127.0.0.1:8000/docs




🌍 Frontend (Static Site)

cd frontend
python -m http.server 5500
Visit: http://127.0.0.1:5500/index.html


🧠 ML Model
Model used: GradientBoostingClassifier from scikit-learn

Trained on 10,000-row synthetic dataset with features like:

Credit Score, Age Group, Income, Family Background, etc.

Saved as lead_intent_model.pkl

🛡️ Reranker Logic (LLM-Inspired)
Adjusts scores using keywords in the "Comment" field:

"urgent" → +15

"interested" → +10

"not interested" → −10

"price too high" → −10
 
 and if the entered lead description does not match with the declared list, it switches to LLM and then gets the job done. 



📂 Project Structure

lead-scoring-app/
├── backend/        # FastAPI + ML model
├── frontend/       # HTML + CSS + JS (form UI)
├── model/          # Training script (optional)
├── data/           # Dataset CSV (optional)


📦 Deployment
Backend hosted on Render
            &  
Frontend deployed via Netlify

URL : https://beamish-daifuku-045978.netlify.app

👤 Author
Pankit Shah
LinkedIn: http://www.linkedin.com/in/pankit-shah13
GitHub: https://github.com/Shah-Pankit

📄 License
MIT License
