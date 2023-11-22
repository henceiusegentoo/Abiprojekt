mod rocket;
mod physics;

use std::collections::HashMap;
use physics::*;

use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn simulate(fuel: f64, thrust_duration: f64, time_increments: f64) -> HashMap<&'static str, HashMap<&'static str, f64>> {
    let mut rocket = rocket::Rocket::new(
        200_000 as f64,
        (650 * 33) as f64,
        (2_300_000 * 33) as f64,
        100_000 as f64,
        0 as f64,
        0 as f64,
        0.75 as f64,
        63.62 as f64,
    );

    rocket.set_fuel(fuel);
    rocket.set_thrust_duration(thrust_duration);

    let mut points_in_time = Vec::new();

    let mut time = 0 as f64;
    let mut distance = 0 as f64;
    let mut velocity = 0 as f64;
    let mut acceleration = 0 as f64;

    let mut pre_thrust = HashMap::new();
    pre_thrust.insert("time", time);
    pre_thrust.insert("distance", distance);
    pre_thrust.insert("velocity", velocity);
    pre_thrust.insert("acceleration", acceleration);
    pre_thrust.insert("weight", rocket.get_total_weight());

    let rounding_precision = -(time_increments.log10().round() as i32);

    // Part 1 - Thrust
    while rocket.get_fuel() > 0.0 && rocket.get_thrust_duration() > time {
        let fuel = rocket.get_fuel();

        let drag = physics::get_drag_force(
            velocity,
            distance,
            rocket.get_drag_coefficient(),
            rocket.get_surface_area(),
        );

        acceleration = physics::get_acceleration(
            rocket.get_thrust(),
            rocket.get_total_weight(),
            drag,
        ) - get_scaled_gravity(distance);

        velocity += acceleration * time_increments;
        distance += velocity * time_increments;

        // round time with rounding_precision to avoid floating point errors
        let time_not_rounded = time + time_increments;
        time = round_to_precision(time_not_rounded, rounding_precision);
        points_in_time.push((time, distance));

        let fuel_remaining = fuel - (rocket.get_flow_rate() * time_increments);
        if fuel_remaining < 0.0 {
            rocket.set_fuel(0.0);
        } else {
            rocket.set_fuel(fuel_remaining);
        }
    }

    let mut post_thrust = HashMap::new();
    post_thrust.insert("time", time);
    post_thrust.insert("distance", distance);
    post_thrust.insert("velocity", velocity);
    post_thrust.insert("acceleration", acceleration);
    post_thrust.insert("weight", rocket.get_total_weight());

    // Part 2 - Coasting
    while velocity > 0.0 {
        let drag = physics::get_drag_force(
            velocity,
            distance,
            rocket.get_drag_coefficient(),
            rocket.get_surface_area(),
        );

        acceleration = physics::get_acceleration(
            0.0,
            rocket.get_total_weight(),
            drag,
        ) - get_scaled_gravity(distance);

        velocity += acceleration * time_increments;
        distance += velocity * time_increments;

        // round time with rounding_precision to avoid floating point errors
        let time_not_rounded = time + time_increments;
        time = round_to_precision(time_not_rounded, rounding_precision);
        points_in_time.push((time, distance));
    }

    let mut post_coast = HashMap::new();
    post_coast.insert("time", time);
    post_coast.insert("distance", distance);
    post_coast.insert("velocity", velocity);
    post_coast.insert("acceleration", acceleration);
    post_coast.insert("weight", rocket.get_total_weight());

    let mut stages: HashMap<&str, HashMap<&str, f64>> = HashMap::new();
    stages.insert("pre_thrust", pre_thrust);
    stages.insert("post_thrust", post_thrust);
    stages.insert("post_coast", post_coast);

    return stages;
}

fn round_to_precision(value: f64, precision: i32) -> f64 {
    let precision = 10.0_f64.powi(precision);
    (value * precision).round() / precision
}

/// A Python module implemented in Rust.
#[pymodule]
fn simulation(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(simulate, m)?)?;
    Ok(())
}
