from datetime import datetime, timezone
from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from api.db import Base

class Charger(Base):
    __tablename__ = "chargers"

    charger_id = Column(String, primary_key=True)
    lat = Column(Float)
    lng = Column(Float)
    is_active = Column(Boolean, default=True)

    telemetry = relationship("Telemetry", back_populates="charger")


class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True)
    charger_id = Column(String, ForeignKey("chargers.charger_id"))
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    voltage = Column(Float)
    current = Column(Float)
    connector_temp = Column(Float)
    fan_speed = Column(Integer)
    cabinet_temp = Column(Float)
    charging_power = Column(Float)
    comm_latency = Column(Integer)
    error_code = Column(Integer)
    fault_label = Column(Integer)

    charger = relationship("Charger", back_populates="telemetry")


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)
    charger_id = Column(String)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    risk_score = Column(Float)
    fault_type = Column(Integer)


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    charger_id = Column(String)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    level = Column(String)  # OK / WARNING / CRITICAL
    message = Column(Text)


class MaintenanceLog(Base):
    __tablename__ = "maintenance_logs"

    id = Column(Integer, primary_key=True)
    charger_id = Column(String)
    date = Column(DateTime)

    technician_name = Column(String)
    action_taken = Column(Text)