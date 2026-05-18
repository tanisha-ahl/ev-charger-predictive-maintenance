import joblib
import numpy as np
import os

MODEL_PATH = "ml/models/anomaly_model.pkl"

class AnomalyDetector:
    def __init__(self):
        if not os.path.exists(MODEL_PATH):
            raise Exception("Model not found. Train first.")
        self.model = joblib.load(MODEL_PATH)

    def predict(self, data: dict):
        features = [
            data["voltage"],
            data["current"],
            data["connector_temp"],
            data["fan_speed"],
            data["cabinet_temp"],
            data["charging_power"],
            data["comm_latency"],
            data["error_code"],
        ]

        X = np.array(features).reshape(1, -1)

        prediction = self.model.predict(X)[0]  # 1 or -1

        return {
            "is_anomaly": int(prediction == -1),
            "raw_prediction": int(prediction)
        }