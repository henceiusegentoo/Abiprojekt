pub struct Rocket {
    base_weight: f64,

    flow_rate: f64,
    thrust: f64,

    payload_weight: f64,
    fuel: f64,
    thrust_duration: f64,

    drag_coefficient: f64,
    surface_area: f64,
}

impl Rocket {
    pub fn new(
        base_weight: f64,

        flow_rate: f64,
        thrust: f64,

        payload_weight: f64,
        fuel: f64,
        thrust_duration: f64,

        drag_coefficient: f64,
        surface_area: f64,
    ) -> Rocket {
        Rocket {
            base_weight: base_weight,
            payload_weight: payload_weight,
            fuel: fuel,
            thrust_duration: thrust_duration,
            flow_rate: flow_rate,
            thrust: thrust,
            drag_coefficient: drag_coefficient,
            surface_area: surface_area,
        }
    }

    pub fn set_fuel(&mut self, fuel: f64) {
        self.fuel = fuel;
    }

    pub fn get_fuel(&self) -> f64 {
        return self.fuel;
    }

    pub fn set_thrust_duration(&mut self, thrust_duration: f64) {
        self.thrust_duration = thrust_duration;
    }

    pub fn get_thrust_duration(&self) -> f64 {
        return self.thrust_duration;
    }

    pub fn get_total_weight(&self) -> f64 {
        return self.base_weight + self.payload_weight + self.fuel;
    }

    pub fn get_thrust(&self) -> f64 {
        return self.thrust;
    }

    pub fn get_flow_rate(&self) -> f64 {
        return self.flow_rate;
    }

    pub fn get_drag_coefficient(&self) -> f64 {
        return self.drag_coefficient;
    }

    pub fn get_surface_area(&self) -> f64 {
        return self.surface_area;
    }
}