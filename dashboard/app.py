import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="EV Charger Monitoring", layout="wide")

st.title("⚡ EV Charger Predictive Maintenance Dashboard")

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# 🔄 Refresh button
if st.button("Refresh Data"):
    st.experimental_rerun()

# 📊 Load telemetry
telemetry = pd.read_sql("SELECT * FROM telemetry ORDER BY timestamp DESC LIMIT 100", engine)

# 🚨 Load alerts
alerts = pd.read_sql("SELECT * FROM alerts ORDER BY timestamp DESC LIMIT 20", engine)

# 📈 Load predictions
predictions = pd.read_sql("SELECT * FROM predictions ORDER BY timestamp DESC LIMIT 100", engine)

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Latest Telemetry")
    st.dataframe(telemetry)

with col2:
    st.subheader("🚨 Recent Alerts")
    st.dataframe(alerts)

st.subheader("📈 Predictions")
st.dataframe(predictions)

# Chart
st.subheader("📉 Temperature Trend")
if not telemetry.empty:
    st.line_chart(telemetry.set_index("timestamp")["connector_temp"])