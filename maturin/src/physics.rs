use std::collections::HashMap;

pub fn get_acceleration(thrust: f64, mass: f64, drag: f64) -> f64 {
    return (thrust - drag) / mass;
}

pub fn get_scaled_gravity(distance: f64) -> f64 {
    return get_earth_gravity() * (get_earth_radius() / (get_earth_radius() + distance)).powi(2);
}

fn get_scaled_air_density(distance: f64) -> f64 {
    let mut air_density_at_height = HashMap::new();

    air_density_at_height.insert(-2000, 1.47808);
    air_density_at_height.insert(-1000, 1.34700);
    air_density_at_height.insert(0, 1.225);
    air_density_at_height.insert(1000, 1.11164);
    air_density_at_height.insert(2000, 1.00649);
    air_density_at_height.insert(3000, 9.09122e-1);
    air_density_at_height.insert(4000, 8.19129e-1);
    air_density_at_height.insert(5000, 7.36116e-1);
    air_density_at_height.insert(6000, 6.59697e-1);
    air_density_at_height.insert(7000, 5.89501e-1);
    air_density_at_height.insert(8000, 5.25168e-1);
    air_density_at_height.insert(9000, 4.66348e-1);
    air_density_at_height.insert(10000, 4.12707e-1);
    air_density_at_height.insert(12000, 3.10828e-1);
    air_density_at_height.insert(15000, 1.93674e-1);
    air_density_at_height.insert(20000, 8.80349e-2);
    air_density_at_height.insert(25000, 3.94658e-2);
    air_density_at_height.insert(30000, 1.80119e-2);
    air_density_at_height.insert(35000, 8.21392e-3);
    air_density_at_height.insert(40000, 3.85101e-3);
    air_density_at_height.insert(45000, 1.88129e-3);
    air_density_at_height.insert(50000, 9.77525e-4);
    air_density_at_height.insert(60000, 2.88321e-4);
    air_density_at_height.insert(70000, 7.42430e-5);
    air_density_at_height.insert(80000, 1.57005e-5);
    air_density_at_height.insert(84852, 6.95788e-6);

    if distance < -2000.0 {
        return air_density_at_height[&-2000];
    } else if distance > 84852.0 {
        return air_density_at_height[&84852];
    } else {      
        let closest_key = air_density_at_height.keys().min_by(|a, b| (*a - distance as i64).abs().partial_cmp(&(*b - distance as i64).abs()).unwrap());

        match closest_key {
            Some(key) => return air_density_at_height[key],
            None => return 0.0,
        }
    }
}

pub fn get_drag_force(velocity: f64, distance: f64, drag_coefficient: f64, surface_area: f64) -> f64 {
    return 0.5 * drag_coefficient * get_scaled_air_density(distance) * surface_area * velocity.powi(2);
}

fn get_earth_gravity() -> f64 {
    return 9.78032;
}

fn get_earth_radius() -> f64 {
    return 6378100 as f64;
}
