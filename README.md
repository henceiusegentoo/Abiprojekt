# Instructions
**Configuration is done in config.toml**
* Fuel is in kg
* Thrust duration in seconds
* Payload weight in kg
* Desired height is in metres
* Iteration is just an int

## Example
```toml
[rocket_parameters]
fuel = 3_400_000.0
thrust_duration = 240.0
payload_weight = 100_000

[simulation_conditions]
desired_height = 5000_000.0
iterations = 100_000
```
