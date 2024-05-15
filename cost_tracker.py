from datetime import datetime, timedelta
from machine import Machine

class CostTracker:
    TYPE1_COST_PER_MINUTE = 1
    TYPE2_COST_PER_MINUTE = 2
    DATETIME_FORMAT = "%m-%d-%Y %H:%M:%S.%f"

    def __init__(self):
        self.machines = {}

    def create_machine(self, name, machine_type):
        try:
            if name in self.machines:
                raise ValueError(f"Machine {name} already exists.")
            self.machines[name] = Machine(name, machine_type)
            self.machines[name].start()
            current_time = datetime.now().strftime(self.DATETIME_FORMAT)[:-3]
            print(f"{current_time}:: Machine {name} of type {machine_type} created.")
        except Exception as e:
            print(f"Error creating machine {name}: {e}")

    def delete_machine(self, name):
        try:
            if name not in self.machines:
                raise ValueError(f"Machine {name} does not exist.")
            self.machines.pop(name)
            current_time = datetime.now().strftime(self.DATETIME_FORMAT)[:-3]
            print(f"{current_time}:: Machine {name} deleted.")
        except Exception as e:
            print(f"Error deleting machine {name}: {e}")

    def start_machine(self, name):
        try:
            if name not in self.machines:
                raise ValueError(f"Machine {name} does not exist.")
            self.machines[name].start()
            current_time = datetime.now().strftime(self.DATETIME_FORMAT)[:-3]
            print(f"{current_time}:: Machine {name} started.")
        except Exception as e:
            print(f"Error starting machine {name}: {e}")

    def stop_machine(self, name):
        try:
            if name not in self.machines:
                raise ValueError(f"Machine {name} does not exist.")
            self.machines[name].stop()
            current_time = datetime.now().strftime(self.DATETIME_FORMAT)[:-3]
            print(f"{current_time}:: Machine {name} stopped.")
        except Exception as e:
            print(f"Error stopping machine {name}: {e}")

    def get_machine_cost(self, name):
        try:
            if name not in self.machines:
                raise ValueError(f"Machine {name} does not exist.")
            machine = self.machines[name]
            uptime_minutes = machine.get_uptime().total_seconds() // 60
            if machine.machine_type == 'type 1':
                return uptime_minutes * self.TYPE1_COST_PER_MINUTE
            elif machine.machine_type == 'type 2':
                return uptime_minutes * self.TYPE2_COST_PER_MINUTE
            return 0
        except Exception as e:
            print(f"Error getting cost for machine {name}: {e}")
            return None

    def get_total_cost(self):
        total_cost = 0
        for machine in self.machines.values():
            try:
                uptime_minutes = machine.get_uptime().total_seconds() // 60
                if machine.machine_type == 'type 1':
                    total_cost += uptime_minutes * self.TYPE1_COST_PER_MINUTE
                elif machine.machine_type == 'type 2':
                    total_cost += uptime_minutes * self.TYPE2_COST_PER_MINUTE
            except Exception as e:
                print(f"Error calculating cost for machine {machine.name}: {e}")
        return total_cost

    def get_machines_names(self):
        return list(self.machines.keys())
