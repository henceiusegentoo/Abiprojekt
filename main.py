from simulation import simulate
from optimization.main import optimize
import json
import matplotlib.pyplot as plt
import toml
import os

with open("config.toml") as f:
    config = toml.load(f)

fuel = config["rocket_parameters"]["fuel"] # kg
thrust_duration = config["rocket_parameters"]["thrust_duration"] # s
precision = config["simulation_conditions"]["precision"] # s
desired_height = config["simulation_conditions"]["desired_height"] # m
iterations = config["optimization_conditions"]["iterations"]

print(f"Optimizing for {iterations} iterations with a precision of {precision} seconds per step and a desired height of {desired_height} metres...")

res = optimize(simulate, fuel, thrust_duration, precision, desired_height, iterations)
final_res = simulate(res[0], res[1], precision)

if not os.path.exists("results"):
    os.mkdir("results")

with open("results/data.json", "w") as f:
    json.dump(final_res, f, indent=4)

"""
Output Data format:
time
distance
velocity
acceleration 
weight
"""