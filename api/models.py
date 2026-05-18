from pydantic import BaseModel
from datetime import datetime

class TelemetryPayload(BaseModel):
    charger_id: str
    timestamp: str

    voltage: float
    current: float
    connector_temp: float
    fan_speed: int
    cabinet_temp: float
    charging_power: float
    comm_latency: int
    error_code: int
    fault_label: int