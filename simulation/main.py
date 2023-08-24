from simulation.rocket import Rocket
from simulation.physics import *

rocket = Rocket(
    base_weight=200_000,
    flow_rate=650 * 33,
    thrust=2_300_000 * 33,
)

def simulate(fuel: float, thrust_duration: int, payload_weight: float):
    """
    Simulates the flight of a rocket.

    Parameters
    ----------
    fuel : float
        The amount of fuel to use.

    thrust_duration : int
        The amount of time to use the thrust.

    payload_weight : float
        The weight of the payload.
    """

    rocket.set_payload_weight(payload_weight)
    rocket.set_fuel(fuel)
    rocket.set_thrust_duration(thrust_duration)

    t = 0
    d = 0
    v = 0
    a = 0

    # Part 1 - Thrust
    while (fuel := rocket.get_fuel()) > 0 and rocket.get_thrust_duration() > t:
        drag = get_drag_force(v, d)
        a = get_acceleration(rocket, drag) - get_scaled_gravity(d)
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
        drag = get_drag_force(v, d)
        a = -get_scaled_gravity(d) - (drag / rocket.get_total_weight())

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

    return final.get('distance')