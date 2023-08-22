from simulation.rocket import Rocket
from simulation.physics import *

rocket = Rocket(
    base_weight=200_000,
    payload_weight=100_000,
    flow_rate=650 * 33,
    thrust=2_300_000 * 33
)

def simulate(fuel: float, thrust_duration: int):
    rocket.set_fuel(fuel)
    rocket.set_thrust_duration(140)

    t = 0
    d = 0
    v = 0
    a = 0

    # Part 1 - Thrust
    while (fuel := rocket.get_fuel()) > 0 and rocket.get_thrust_duration() > t:
        a = get_acceleration(rocket) - get_scaled_gravity(d)
        rocket.set_fuel(fuel - rocket.get_flow_rate())

        v += a
        d += v

        t += 1

    post_thrust = {
        "time": t,
        "distance": d,
        "velocity": v,
        "acceleration": a
    }

    # Part 2 - Free fall
    while v > 0:
        a = -get_scaled_gravity(d)

        v += a
        d += v

        t += 1

    post_free_fall = {
        "time": t,
        "distance": d,
        "velocity": v,
        "acceleration": a
    }

    final = {'distance': d, 'time': t}

    return post_thrust, post_free_fall, final