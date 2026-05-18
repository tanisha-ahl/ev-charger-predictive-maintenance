import csv
from simulator.charger import ChargerSimulator, FaultType

def generate_dataset(filename="data/synthetic/data.csv", samples=1000):
    charger = ChargerSimulator("CHG_0001")

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow([
            "voltage", "current", "connector_temp", "fan_speed",
            "cabinet_temp", "charging_power", "comm_latency",
            "error_code", "fault_label"
        ])

        for i in range(samples):

            # Inject fault randomly
            if i % 200 == 0 and i != 0:
                charger.inject_fault(FaultType.OVERHEATING_CABLE)

            if i % 250 == 0 and i != 0:
                charger.clear_fault()

            data = charger.emit()

            writer.writerow([
                data["voltage"],
                data["current"],
                data["connector_temp"],
                data["fan_speed"],
                data["cabinet_temp"],
                data["charging_power"],
                data["comm_latency"],
                data["error_code"],
                data["fault_label"],
            ])

    print(f"Dataset saved to {filename}")


if __name__ == "__main__":
    generate_dataset()