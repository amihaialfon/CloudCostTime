from datetime import timedelta, datetime
from machine import Machine


class CostTracker:
    type1 = 'type 1'
    type2 = 'type 2'

    def __init__(self):
        self.machines = {}

    def create_machine(self, name, machine_type):
        self.machines[name] = Machine(name, machine_type)
        self.machines[name].start()
        current_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        print(f"{current_time}:: Machine {name} of type {machine_type} created.")

    def delete_machine(self, name):
        if name in self.machines:
            self.machines.pop(name)
            current_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            print(f"{current_time}:: Machine {name} deleted.")
        else:
            current_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            print(f"{current_time}:: Machine {name} does not exist.")

    def start_machine(self, name):
        if name in self.machines:
            self.machines[name].start()
            current_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            print(f"{current_time}:: Machine {name} started.")
        else:
            current_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            print(f"{current_time}:: Machine {name} does not exist.")

    def stop_machine(self, name):
        if name in self.machines:
            self.machines[name].stop()
            current_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            print(f"{current_time}:: Machine {name} stopped.")
        else:
            current_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            print(f"{current_time}:: Machine {name} does not exist.")

    def get_machine_cost(self, name):
        if name in self.machines:
            machine = self.machines[name]
            if machine.start_time:
                uptime_minutes = machine.get_uptime().total_seconds() // 60
                if machine.machine_type == self.type1:
                    return uptime_minutes * 1
                elif machine.machine_type == self.type2:
                    return uptime_minutes * 2
            else:
                return 0
        else:
            current_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            print(f"{current_time}:: Try to get cost for machine {name} and it does not exist.")
            return None

    def get_total_cost(self):
        total_cost = 0
        for machine in self.machines.values():
            if machine.start_time:
                uptime_minutes = machine.get_uptime().total_seconds() // 60
                if machine.machine_type == self.type1:
                    total_cost += uptime_minutes * 1
                elif machine.machine_type == self.type2:
                    total_cost += uptime_minutes * 2
        return total_cost

    def get_machines_names(self):
        return list(self.machines.keys())
