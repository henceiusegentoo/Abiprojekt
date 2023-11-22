import random

def optimize(sim_function, max_fuel: float, max_thrust_duration: int, precision: float, desired_height: float, iterations: int):
    best_params = ()
    
    best = (0, 0) # (height, weight)
    for i in range(iterations):
        if i % 10 == 0:
            print(f"Iteration {i} of {iterations}", end="\r")

        fuel = random.uniform(0, max_fuel)
        thrust_duration = random.uniform(0, max_thrust_duration)

        res = sim_function(fuel, thrust_duration, precision)[-1]
        current = (res[1], res[-1])

        if current[0] > best[0]:
            best = current

            best_params = (fuel, thrust_duration)

        elif current[0] >= best[0] and current[1] < best[1]:
            best = current

            best_params = (fuel, thrust_duration)

        if current[0] >= desired_height:
            max_fuel = fuel
            max_thrust_duration = thrust_duration

            best = (best[0] / 2, best[1] / 2)

    return best_params