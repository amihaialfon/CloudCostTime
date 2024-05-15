import sys
import time
from cost_tracker import CostTracker


def main():
    sys.stdout = open("log.txt", "a")
    print("Start Main: ")

    cost_tracker = CostTracker()

    try:
        cost_tracker.create_machine("a1", "type 1")
        cost_tracker.create_machine("b1", "type 1")
        time.sleep(60)
        cost_tracker.create_machine("c1", "type 1")
        cost_tracker.create_machine("d2", "type 2")

        cost_tracker.start_machine("a1")
        cost_tracker.start_machine("b1")
        cost_tracker.start_machine("c1")
        cost_tracker.start_machine("d2")

        time.sleep(60)

        print(f"Total cost: ${cost_tracker.get_total_cost()}")
        cost_tracker.stop_machine("b1")
        print(f"Total cost: ${cost_tracker.get_total_cost()}")
        print(f"Cost of machine a1: ${cost_tracker.get_machine_cost('a1')}")
        print(f"Cost of machine d2: ${cost_tracker.get_machine_cost('d2')}")
        print(f"List of machines: {cost_tracker.get_machines_names()}")

    except Exception as e:
        print(f"An error occurred in main: {e}")


if __name__ == "__main__":
    main()
