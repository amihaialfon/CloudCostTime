#to run flask: python app.py and than you call this apis from postman

from flask import Flask, jsonify, request
from cost_tracker import CostTracker
import sys

app = Flask(__name__)
cost_tracker = CostTracker()
sys.stdout = open("log.txt", "a")

@app.route("/create_machine", methods=["POST"])
def create_machine():
    data = request.json
    name = data["name"]
    machine_type = data["type"]
    cost_tracker.create_machine(name, machine_type)
    return jsonify({"message": f"Machine {name} of type {machine_type} created."})

@app.route("/delete_machine/<name>", methods=["DELETE"])
def delete_machine(name):
    cost_tracker.delete_machine(name)
    return jsonify({"message": f"Machine {name} deleted."})

@app.route("/start_machine/<name>", methods=["POST"])
def start_machine(name):
    cost_tracker.start_machine(name)
    return jsonify({"message": f"Machine {name} started."})

@app.route("/stop_machine/<name>", methods=["POST"])
def stop_machine(name):
    cost_tracker.stop_machine(name)
    return jsonify({"message": f"Machine {name} stopped."})

@app.route("/get_machine_cost/<name>")
def get_machine_cost(name):
    cost = cost_tracker.get_machine_cost(name)
    return jsonify({"cost": cost})

@app.route("/get_total_cost")
def get_total_cost():
    total_cost = cost_tracker.get_total_cost()
    return jsonify({"total_cost": total_cost})

@app.route("/get_machines_names")
def get_machines_names():
    names = cost_tracker.get_machines_names()
    return jsonify({"machines": names})

if __name__ == "__main__":
    app.run(debug=True)
