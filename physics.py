from constants import *
from rocket import Rocket

def get_acceleration(rocket: Rocket) -> float:
    """
    Returns the acceleration of an object with the given mass at the given height.

    Parameters
    ----------
    rocket : Rocket
        The rocket to calculate the acceleration of.
    """
    return rocket.thrust / rocket.get_total_weight()

def get_scaled_gravity(distance: float) -> float:
    """
    Returns the gravity at the given distance from the earth's core.

    Parameters
    ----------
    distance : float
        The distance from the earth's surface in m.
    """
    return EARTH_GRAVITY * (EARTH_RADIUS / (EARTH_RADIUS + distance)) ** 2