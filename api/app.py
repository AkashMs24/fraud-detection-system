from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="Cost-Sensitive-Real-Time-Fraud-Detection-Decision-System
 API")

class Transaction(BaseModel):
    Time: float
    Amount: float
    V1: float = 0.0
    V2: float = 0.0
    V3: float = 0.0
    V4: float = 0.0
    V5: float = 0.0
    V6: float = 0.0
    V7: float = 0.0
    V8: float = 0.0
    V9: float = 0.0
    V10: float = 0.0
    V11: float = 0.0
    V12: float = 0.0
    V13: float = 0.0
    V14: float = 0.0
    V15: float = 0.0
    V16: float = 0.0
    V17: float = 0.0
    V18: float = 0.0
    V19: float = 0.0
    V20: float = 0.0
    V21: float = 0.0
    V22: float = 0.0
    V23: float = 0.0
    V24: float = 0.0
    V25: float = 0.0
    V26: float = 0.0
    V27: float = 0.0
    V28: float = 0.0

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/predict_fraud")
def predict_fraud(txn: Transaction):
    # Dummy logic (replace with model later)
    risk_score = min(1.0, txn.Amount / 5000)

    if risk_score > 0.7:
        decision = "HIGH RISK"
    elif risk_score > 0.4:
        decision = "MEDIUM RISK"
    else:
        decision = "LOW RISK"

    return {
        "fraud_probability": round(risk_score, 3),
        "risk_level": decision
    }
