import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

DATA_PATH = "data/synthetic/data.csv"
MODEL_PATH = "ml/models/anomaly_model.pkl"

def train_model():
    df = pd.read_csv(DATA_PATH)

    # Features (exclude label)
    X = df.drop(columns=["fault_label"])

    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,
        random_state=42
    )

    model.fit(X)

    # Create model directory if not exists
    os.makedirs("ml/models", exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    train_model()