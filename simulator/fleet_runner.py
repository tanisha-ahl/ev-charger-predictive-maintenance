import time
import requests
from simulator.charger import ChargerSimulator
from simulator.fault_injector import FaultScheduler

API_URL = "http://127.0.0.1:8000/ingest"

def run_fleet(num_chargers=5, steps=20):
    chargers = [ChargerSimulator(f"CHG_{i:04d}") for i in range(1, num_chargers + 1)]
    scheduler = FaultScheduler()

    for step in range(steps):
        print(f"\n=== STEP {step} ===")

        scheduler.tick(chargers)

        for c in chargers:
            data = c.emit()

            try:
                res = requests.post(API_URL, json=data)
                print(res.json())
            except Exception as e:
                print("API ERROR:", e)

        time.sleep(1)

if __name__ == "__main__":
    run_fleet()