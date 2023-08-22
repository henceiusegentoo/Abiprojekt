from simulation.main import simulate

fuel = 3_400_000 # kg
thrust_duration = 140 # s
payload_weight = 100_000 # kg

res = simulate(fuel, thrust_duration, payload_weight)

print(res[2])