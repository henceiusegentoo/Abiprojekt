from simulation.main import simulate

fuel = 3_400_000.0
thrust_duration = 10

res = simulate(fuel, thrust_duration, 0.01)

for val, key in res.items():
    print(f"{val}: {key}")