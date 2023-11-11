from simulation.main import simulate
from optimization.main import optimize
import tomllib
import os
import matplotlib.pyplot as plt

config_path = os.path.join(os.path.dirname(__file__), "config.toml")
if not os.path.exists(config_path):
    raise FileNotFoundError("Config file not found")

with open(config_path, "rb") as config_file:
    config = tomllib.load(config_file)

# fuel in kg
# thrust_duration in s
# payload_weight in kg
# desired_height in m
# iterations as int

fuel = config["rocket_parameters"]["fuel"]
thrust_duration = config["rocket_parameters"]["thrust_duration"]
payload_weight = config["rocket_parameters"]["payload_weight"]

desired_height = config["simulation_conditions"]["desired_height"]
iterations = config["simulation_conditions"]["iterations"]

def main():
    optimization = optimize(
        f = simulate,
        max_fuel=fuel,
        max_thrust_duration=thrust_duration,
        payload_weight=payload_weight,
        desired_height=desired_height,
        iterations=iterations
    )

    final_fuel = optimization[0]
    final_thrust_duration = optimization[1]
    final_payload_weight = optimization[2]

    print(f"Optimized fuel: {final_fuel:_}")
    print(f"Optimized thrust duration: {final_thrust_duration:_}")
    print(f"Optimized payload weight: {final_payload_weight:_}")

    res = simulate(
        fuel = final_fuel,
        thrust_duration = final_thrust_duration,
        payload_weight = final_payload_weight
    )

    plt.plot([t[0] for t in res[1]], [t[1] for t in res[1]])
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")
    plt.savefig("height.png")

    print(f"Final distance: {res[1]}")

if __name__ == "__main__":
    main()