from simulation.rocket import Rocket
from simulation.physics import *
import math

# Data of the rocket taken from the SpaceX Super Heavy Starship
rocket = Rocket(
    base_weight=200_000,  # kg # Weight of the rocket without fuel and payload
    flow_rate=650 * 33,  # kg/s # Fuel flow rate per engine
    thrust=2_300_000 * 33,  # N # Thrust per engine
    payload_weight=100_000,  # kg # Usual weight of the payload
)


def simulate(fuel: float, thrust_duration: int, time_increments: float = 1):
    """
    Simulates the flight of a rocket.
    """

    rocket.set_fuel(fuel)
    rocket.set_thrust_duration(thrust_duration)

    points_in_time = []

    time = 0
    distance = 0
    velocity = 0
    acceleration = 0

    pre_thrust = {
        "time": time,
        "distance": distance,
        "velocity": velocity,
        "acceleration": acceleration,
        "weight": rocket.get_total_weight(),
    }

    # Part 1 - Thrust
    while (fuel := rocket.get_fuel()) > 0 and rocket.get_thrust_duration() > time:
        drag = get_drag_force(velocity, distance)
        acceleration = get_acceleration(
            rocket.get_thrust(), rocket.get_total_weight(), drag
        ) - get_scaled_gravity(distance)

        rounding_precision = -int(round(math.log10(time_increments)))

        velocity += acceleration * time_increments
        distance += velocity * time_increments
        
        time = round(time + time_increments, rounding_precision) # round to avoid floating point errors
        points_in_time.append((time, distance))

        fuel_remaining = fuel - rocket.get_flow_rate() * time_increments

        rocket.set_fuel(fuel_remaining) if fuel_remaining > 0 else rocket.set_fuel(0)

    post_thrust = {
        "time": time,
        "distance": distance,
        "velocity": velocity,
        "acceleration": acceleration,
        "weight": rocket.get_total_weight(),
    }

    # Part 2 - Free fall
    while velocity > 0:
        drag = get_drag_force(velocity, distance)
        acceleration = -get_scaled_gravity(distance) - (drag / rocket.get_total_weight())

        rounding_precision = -int(round(math.log10(time_increments)))

        velocity += acceleration * time_increments
        distance += velocity * time_increments

        time = round(time + time_increments, rounding_precision) # round to avoid floating point errors
        points_in_time.append((time, distance))

    post_free_fall = {
        "time": time,
        "distance": distance,
        "velocity": velocity,
        "acceleration": acceleration,
        "weight": rocket.get_total_weight(),
    }

    return {
        "points_in_time": points_in_time,
        "pre_thrust": pre_thrust,
        "post_thrust": post_thrust,
        "post_free_fall": post_free_fall,
    }