from simulation.main import simulate
from optimization.main import optimize
import json
import matplotlib.pyplot as plt

fuel = 3_400_000.0
thrust_duration = 1000
precision = 1
desired_height = 384_400_000
iterations = 1000

res = optimize(simulate, fuel, thrust_duration, precision, desired_height, iterations)

final_res = simulate(res[0], res[1], precision)

with open("data.json", "w") as f:
    json.dump(final_res, f, indent=2)

# plt.plot([x[0] for x in final_res["points_in_time"]], [x[1] for x in final_res["points_in_time"]])
# plt.legend(["Distance"])
# plt.xlabel("Time")
# plt.savefig("distance.png")