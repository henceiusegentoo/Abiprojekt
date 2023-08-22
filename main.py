from simulation.main import simulate

fuel = 3_400_000 # kg
thrust_duration = 140 # s

res = simulate(fuel, thrust_duration)

print(res[2])