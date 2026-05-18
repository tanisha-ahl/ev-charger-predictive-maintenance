from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from api.models import TelemetryPayload
from api.db import get_db
from api.db_models import Charger, Telemetry, Prediction, Alert
from ml.inference import AnomalyDetector

router = APIRouter()

detector = AnomalyDetector()

@router.post("/ingest")
def ingest(payload: TelemetryPayload, db: Session = Depends(get_db)):

    # Check charger
    charger = db.query(Charger).filter(
        Charger.charger_id == payload.charger_id
    ).first()

    if not charger:
        raise HTTPException(status_code=404, detail="Charger not registered")

    # Store telemetry
    record = Telemetry(
        charger_id=payload.charger_id,
        timestamp=datetime.fromisoformat(payload.timestamp.replace("Z", "+00:00")),
        voltage=payload.voltage,
        current=payload.current,
        connector_temp=payload.connector_temp,
        fan_speed=payload.fan_speed,
        cabinet_temp=payload.cabinet_temp,
        charging_power=payload.charging_power,
        comm_latency=payload.comm_latency,
        error_code=payload.error_code,
        fault_label=payload.fault_label,
    )

    db.add(record)

    # 🔥 Run ML inference
    result = detector.predict(payload.dict())

    # Store prediction
    prediction = Prediction(
        charger_id=payload.charger_id,
        risk_score=float(result["is_anomaly"]),
        fault_type=payload.fault_label
    )
    db.add(prediction)

    # 🚨 Generate alert if anomaly
    if result["is_anomaly"]:
        alert = Alert(
            charger_id=payload.charger_id,
            level="CRITICAL",
            message=f"Anomaly detected for charger {payload.charger_id}"
        )
        db.add(alert)

    db.commit()

    return {
        "status": "stored",
        "anomaly": result["is_anomaly"]
    }