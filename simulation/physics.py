from simulation.constants import *
from simulation.rocket import Rocket

def get_acceleration(rocket: Rocket, drag: float) -> float:
    """
    Returns the acceleration of an object with the given mass at the given height.

    Parameters
    ----------
    rocket : Rocket
        The rocket to calculate the acceleration of.

    drag : float
        The drag force acting on the rocket.
    """
    return (rocket.thrust - drag) / rocket.get_total_weight()

def get_scaled_gravity(distance: float) -> float:
    """
    Returns the gravity at the given distance from the earth's core.

    Parameters
    ----------
    distance : float
        The distance from the earth's surface in m.
    """
    return EARTH_GRAVITY * (EARTH_RADIUS / (EARTH_RADIUS + distance)) ** 2

def get_scaled_air_density(distance: float) -> float:
    """
    Returns the air density at the given distance from the earth's core.

    Parameters
    ----------
    distance : float
        The distance from the earth's surface in m.
    """

    air_density_at_height = {
        -2000: 1.47808,
        -1000: 1.34700,
        0: 1.225,
        1000: 1.11164,
        2000: 1.00649,
        3000: 9.09122e-1,
        4000: 8.19129e-1,
        5000: 7.36116e-1,
        6000: 6.59697e-1,
        7000: 5.89501e-1,
        8000: 5.25168e-1,
        9000: 4.66348e-1,
        10000: 4.12707e-1,
        12000: 3.10828e-1,
        15000: 1.93674e-1,
        20000: 8.80349e-2,
        25000: 3.94658e-2,
        30000: 1.80119e-2,
        35000: 8.21392e-3,
        40000: 3.85101e-3,
        45000: 1.88129e-3,
        50000: 9.77525e-4,
        60000: 2.88321e-4,
        70000: 7.42430e-5,
        80000: 1.57005e-5,
        84852: 6.95788e-6
    }

    if distance < -2000:
        return air_density_at_height[-2000]
    
    elif distance > 84852:
        return air_density_at_height[84852]
    
    else:
        return air_density_at_height[min(air_density_at_height.keys(), key=lambda x:abs(x-distance))]


def get_drag_force(velocity: float, distance: float) -> float:
    """
    Returns the drag force on an object with the given velocity.

    Parameters
    ----------
    velocity : float
        The velocity of the object in m/s.

    distance : float
        The distance from the earth's surface in m.
    """

    return 0.5 * DRAG_COEFFICIENT * get_scaled_air_density(distance) * SURFACE_AREA * velocity ** 2