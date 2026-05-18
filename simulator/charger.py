# (PASTE EXACTLY — no changes)
import random
import math
from datetime import datetime, timezone
from enum import IntEnum

NORMAL_PARAMS = {
    "voltage": {"mean": 400, "std": 10, "min": 300, "max": 480},
    "current": {"mean": 32, "std": 3, "min": 0, "max": 63},
    "connector_temp": {"mean": 35, "std": 5, "min": 20, "max": 60},
    "fan_speed": {"mean": 1500, "std": 200, "min": 500, "max": 3000},
    "cabinet_temp": {"mean": 40, "std": 5, "min": 15, "max": 75},
    "charging_power": {"mean": 22, "std": 2, "min": 0, "max": 50},
    "comm_latency": {"mean": 50, "std": 15, "min": 5, "max": 500},
}

class FaultType(IntEnum):
    NORMAL = 0
    OVERHEATING_CABLE = 1
    POWER_DEGRADATION = 2
    COOLING_FAULT = 3
    UNSTABLE_VOLTAGE = 4
    INTERMITTENT_DISCONNECT = 5

FAULT_NAMES = {
    FaultType.NORMAL: "NORMAL",
    FaultType.OVERHEATING_CABLE: "OVERHEATING_CABLE",
    FaultType.POWER_DEGRADATION: "POWER_DEGRADATION",
    FaultType.COOLING_FAULT: "COOLING_FAULT",
    FaultType.UNSTABLE_VOLTAGE: "UNSTABLE_VOLTAGE",
    FaultType.INTERMITTENT_DISCONNECT: "INTERMITTENT_DISCONNECT",
}

class ChargerSimulator:
    def __init__(self, charger_id: str):
        self.charger_id = charger_id
        self.step = 0
        self.fault_type = FaultType.NORMAL
        self.fault_start_step = None

    def inject_fault(self, fault_type: FaultType):
        self.fault_type = fault_type
        self.fault_start_step = self.step

    def clear_fault(self):
        self.fault_type = FaultType.NORMAL
        self.fault_start_step = None

    def _sample(self, field: str) -> float:
        p = NORMAL_PARAMS[field]
        val = random.gauss(p["mean"], p["std"])
        return round(max(p["min"], min(p["max"], val)), 2)

    def _normal_reading(self):
        return {
            "voltage": self._sample("voltage"),
            "current": self._sample("current"),
            "connector_temp": self._sample("connector_temp"),
            "fan_speed": int(self._sample("fan_speed")),
            "cabinet_temp": self._sample("cabinet_temp"),
            "charging_power": self._sample("charging_power"),
            "comm_latency": int(self._sample("comm_latency")),
            "error_code": 0,
        }

    def _apply_overheating(self, r):
        steps = self.step - self.fault_start_step
        r["connector_temp"] = min(95, 40 + steps * 5)
        r["error_code"] = 4 if r["connector_temp"] > 80 else 0
        return r

    def emit(self):
        r = self._normal_reading()

        if self.fault_type == FaultType.OVERHEATING_CABLE:
            r = self._apply_overheating(r)

        self.step += 1

        return {
            "charger_id": self.charger_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "fault_label": int(self.fault_type),
            **r,
        }