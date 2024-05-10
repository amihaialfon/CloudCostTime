from datetime import datetime, timedelta

class Machine:
    def __init__(self, name, machine_type):
        self.start_time = None
        self.name = name
        self.machine_type = machine_type

    def start(self):
        self.start_time = datetime.now()

    def stop(self):
        self.start_time = None

    def get_uptime(self):
        if not self.start_time:
            return timedelta(seconds=0)
        return datetime.now() - self.start_time
