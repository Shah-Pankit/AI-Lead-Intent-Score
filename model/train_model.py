import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("..\data\lead_intent_dataset.csv")

# Drop unneeded columns
X = df.drop(columns=["LeadIntent", "Email", "Phone", "Comment"])
y = df["LeadIntent"]

# Categorical and numerical features
categorical_cols = ["AgeGroup", "FamilyBackground", "Profession", "CompanyType", "City"]
numerical_cols = ["CreditScore", "Income"]

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
    ],
    remainder="passthrough"
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", GradientBoostingClassifier(random_state=42))
])

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

# Save trained model
joblib.dump(pipeline, "lead_intent_model.pkl")
print("Model trained and saved as lead_intent_model.pkl")
