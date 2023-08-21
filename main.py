from rocket import Rocket
from physics import * 

rocket = Rocket(
    base_weight=200_000,
    payload_weight=100_000,
    flow_rate=650 * 33,
    thrust=2_300_000 * 33
)

fuel_weight = 3_400_000
rocket.set_fuel(fuel_weight)
rocket.set_thrust_duration(240)

t = 0
d = 0
v = 0
a = 0

# Part 1 - Thrust
while (fuel := rocket.get_fuel()) > 0 and rocket.get_thrust_duration() > t:
    a = get_acceleration(rocket) -get_scaled_gravity(d)
    rocket.set_fuel(fuel - rocket.get_flow_rate())

    v += a
    d += v

    t += 1
print(f"Thrust Phase - Time: {t}s, Distance: {d}m, Velocity: {v}m/s, Acceleration: {a}m/s²")


# Part 2 - Free fall
while v > 0:
    a = -get_scaled_gravity(d)

    v += a
    d += v

    t += 1
print(f"Free Fall Phase - Time: {t}s, Distance: {d}m, Velocity: {v}m/s, Acceleration: {a}m/s²")

print(f"Distance: {d}m / {d / 1000}km")