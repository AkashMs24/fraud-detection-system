from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

FEATURE_ORDER = [
    "Time",
    "V1","V2","V3","V4","V5","V6","V7","V8","V9","V10",
    "V11","V12","V13","V14","V15","V16","V17","V18","V19","V20",
    "V21","V22","V23","V24","V25","V26","V27","V28",
    "Amount"
]


# 🔴 THIS WAS MISSING
app = FastAPI(title="Fraud Detection API")


df = pd.read_csv(
    r"C:\Users\bumik\OneDrive\Documents\New folder (2)\fraud-detection-system\data\raw\creditcard.csv"
)

X = df.drop("Class", axis=1)
y = df["Class"]

X_train, _, y_train, _ = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

scale_pos_weight = (len(y_train) - y_train.sum()) / y_train.sum()

model = XGBClassifier(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    scale_pos_weight=scale_pos_weight,
    objective="binary:logistic",
    eval_metric="auc",
    random_state=42
)

model.fit(X_train, y_train)

# Optimal threshold from Step 6
OPTIMAL_THRESHOLD = 0.25

# ---------------------------
# API definition
# ---------------------------
app = FastAPI(title="Fraud Detection API")

class Transaction(BaseModel):
    Time: float
    Amount: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float

@app.post("/predict_fraud")
def predict_fraud(tx: Transaction):
    data = pd.DataFrame([tx.dict()])
    data = data[FEATURE_ORDER]

    prob = model.predict_proba(data)[0][1]

    if prob >= 0.6:
        decision = "BLOCK"
        risk = "HIGH"
    elif prob >= OPTIMAL_THRESHOLD:
        decision = "REVIEW"
        risk = "MEDIUM"
    else:
        decision = "ALLOW"
        risk = "LOW"

    return {
        "fraud_probability": round(float(prob), 4),
        "risk_level": risk,
        "decision": decision
    }

