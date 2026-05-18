import random
from simulator.charger import ChargerSimulator, FaultType

FAULT_TYPES = [
    FaultType.OVERHEATING_CABLE,
    FaultType.POWER_DEGRADATION,
    FaultType.COOLING_FAULT,
    FaultType.UNSTABLE_VOLTAGE,
    FaultType.INTERMITTENT_DISCONNECT,
]

class FaultScheduler:
    def __init__(self, inject_prob=0.1, fault_duration=5):
        self.inject_prob = inject_prob
        self.fault_duration = fault_duration
        self.active_faults = {}

    def tick(self, chargers):
        for c in chargers:
            cid = c.charger_id

            if cid in self.active_faults:
                self.active_faults[cid] -= 1
                if self.active_faults[cid] <= 0:
                    del self.active_faults[cid]
                    c.clear_fault()
            else:
                if random.random() < self.inject_prob:
                    fault = random.choice(FAULT_TYPES)
                    c.inject_fault(fault)
                    self.active_faults[cid] = self.fault_duration
                    print(f"[FAULT] {cid} → {fault.name}")