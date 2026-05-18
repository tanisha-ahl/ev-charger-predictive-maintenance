# ⚡ AI-Powered EV Charger Predictive Maintenance System

## 📌 Overview
This project is a full-stack real-time EV charger monitoring and predictive maintenance system designed to detect charger faults before they become critical.

The system simulates multiple EV chargers, generates live telemetry, processes data through a FastAPI backend, applies machine learning for anomaly detection, stores data in PostgreSQL, and visualizes system health using a Streamlit dashboard.

---

## 🚀 Key Features

- 🔋 Real-time EV charger telemetry simulation
- ⚠️ Fault injection (overheating, voltage instability, cooling faults)
- 🤖 Machine learning-based anomaly detection using Isolation Forest
- 🌐 FastAPI backend for telemetry ingestion and prediction
- 🛢️ PostgreSQL database for telemetry, predictions, and alerts
- 📊 Streamlit dashboard for live monitoring and visualization
- 🚨 Automated alert generation for detected anomalies

---

## 🧱 System Architecture

Simulator → API Backend → ML Inference Engine → PostgreSQL Database → Dashboard

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Backend:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Machine Learning:** Scikit-learn (Isolation Forest)
- **Dashboard:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
ev-charger-pms/
├── api/
├── simulator/
├── ml/
├── dashboard/
├── data/synthetic/
├── tests/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/tanisha-ahl/ev-charger-predictive-maintenance.git
cd ev-charger-predictive-maintenance
```

### 2️⃣ Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://evpms_user:evpms_pass@localhost:5432/evpms_db
API_KEY=dev-secret-key
API_HOST=0.0.0.0
API_PORT=8000
```

### 5️⃣ Start PostgreSQL

```bash
brew services start postgresql@15
```

### 6️⃣ Run Backend

```bash
uvicorn api.main:app --reload
```

### 7️⃣ Run Dashboard

```bash
streamlit run dashboard/app.py
```

### 8️⃣ Start Simulator

```bash
python -m simulator.fleet_runner
```

---

## 📊 Dashboard Features

- Live telemetry updates
- Charger temperature trends
- Fault alerts
- ML anomaly predictions

---

## 🤖 Machine Learning Model

### Model Used:
**Isolation Forest**

### Purpose:
- Learn normal charger behavior
- Detect unusual patterns
- Trigger predictive maintenance alerts

### Why Isolation Forest?
- Efficient
- Scalable
- No labeled dataset required
- Suitable for anomaly detection

---

## 🔥 Real-Time Workflow

1. Simulator generates telemetry  
2. FastAPI ingests data  
3. ML model evaluates anomaly  
4. Prediction stored in DB  
5. Alerts generated  
6. Dashboard visualizes system  

---

## 📈 Future Improvements

- 🌍 Cloud deployment (AWS / Render)
- 📡 Real IoT sensor integration
- 🔔 SMS/Email notifications
- 🗺️ Charger geolocation mapping
- 📊 Advanced predictive analytics
- 🔐 User authentication

---

## 🎯 Real-World Applications

- EV charging station maintenance
- Industrial predictive maintenance
- IoT fleet monitoring
- Smart energy infrastructure

---

## 👩‍💻 Author

**Tanisha Ahlawat**  
BTech Electrical & Computer Science Engineering  
Focused on AI, Software Engineering, and scalable real-time systems.

---

## 📬 Contact

GitHub: https://github.com/tanisha-ahl

---

# ⭐ If you found this project valuable:
Please consider starring the repository.- Live telemetry updates  
- Charger temperature trends  
- Fault alerts  
- ML anomaly predictions  

---

## 🤖 Machine Learning Model

### Model Used:
**Isolation Forest**

### Purpose:
- Learn normal charger behavior  
- Detect unusual patterns  
- Trigger predictive maintenance alerts  

### Why Isolation Forest?
- Efficient  
- Scalable  
- No labeled dataset required  
- Suitable for anomaly detection  

---

## 🔥 Real-Time Workflow

1. Simulator generates telemetry  
2. FastAPI ingests data  
3. ML model evaluates anomaly  
4. Prediction stored in DB  
5. Alerts generated  
6. Dashboard visualizes system  

---

## 📈 Future Improvements

- 🌍 Cloud deployment (AWS / Render)  
- 📡 Real IoT sensor integration  
- 🔔 SMS/Email notifications  
- 🗺️ Charger geolocation mapping  
- 📊 Advanced predictive analytics  
- 🔐 User authentication  

---

## 🎯 Real-World Applications

- EV charging station maintenance  
- Industrial predictive maintenance  
- IoT fleet monitoring  
- Smart energy infrastructure  

---

## 👩‍💻 Author

**Tanisha Ahlawat**  
BTech Electrical & Computer Science Engineering  
Focused on AI, Software Engineering, and scalable real-time systems.

---

## 📬 Contact

GitHub: https://github.com/tanisha-ahl

---

# ⭐ If you found this project valuable:
Please consider starring the repository.
