import random
from typing import Callable

def optimize(f: Callable, max_fuel: float, max_thrust_duration: float, payload_weight: int, desired_height: float, iterations: int):
    """
    Optimizes the given function f by trying different parameters and returning the best result.

    Parameters
    ----------
    f : typing.Callable
        The function to optimize.
    max_fuel : float
        The maximum amount of fuel to use.

    max_thrust_duration : float
        The maximum amount of time to use the thrust.

    payload_weight : int
        The weight of the payload.

    desired_height : float
        The height to reach.

    iterations : int
        The amount of iterations to run.
    """

    best = 0
    best_params = None

    min_fuel = 0
    min_thrust_duration = 0

    for i in range(iterations):
        if i % 250 == 0:
            print(f"* Iteration {i:_} of {iterations:_}", end="\r")

        fuel = random.randint(min_fuel, int(max_fuel))
        thrust_duration = random.randint(min_thrust_duration, int(max_thrust_duration))

        res = f(fuel, thrust_duration, payload_weight)[0]

        if res > best:
            best = res
            best_params = (fuel, thrust_duration, payload_weight)

            min_fuel = fuel
            min_thrust_duration = thrust_duration

        if best > desired_height:
            best = 0
            best_params = None

            min_fuel = 0
            min_thrust_duration = 0

            max_fuel = fuel
            max_thrust_duration = thrust_duration

    return best_params or (0, 0, 0)