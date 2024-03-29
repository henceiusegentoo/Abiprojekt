from dataclasses import dataclass

@dataclass
class Rocket:
    """
    A rocket with a base weight, payload weight, fuel and thrust duration.
    
    Attributes
    ----------
    base_weight : float
        The base weight of the rocket in kg.

    payload_weight : float
        The payload weight of the rocket in kg.

    flow_rate : float
        The flow rate of the rocket in kg/s

    thrust : float
        The thrust of the rocket in N

    fuel : float = 0
        The fuel amount of the rocket in kg.

    thrust_duration : float = 0
        The thrust duration of the rocket in seconds.

    total_weight : float = 0
        The total weight of the rocket in kg.

        
    Methods
    -------
    set_fuel(fuel)
        Sets the fuel amount of the rocket in kg.

    get_fuel()
        Returns the fuel amount of the rocket in kg.

    set_thrust_duration(thrust_duration)
        Sets the thrust duration of the rocket in seconds.

    get_thrust_duration()
        Returns the thrust duration of the rocket in seconds.

    get_payload_weight()
        Returns the payload weight of the rocket in kg.

    get_total_weight()
        Returns the total weight of the rocket in kg.
    """

    base_weight: float

    flow_rate: float
    thrust: float

    payload_weight: float = 0
    fuel: float = 0
    thrust_duration: float = 0
    
    total_weight: float = 0

    drag_coefficiency: float = 0.75

    def set_fuel(self, fuel):
        self.fuel = fuel
        self.__set_total_weight()

    def get_fuel(self):
        return self.fuel

    def set_thrust_duration(self, thrust_duration):
        self.thrust_duration = thrust_duration

    def get_thrust_duration(self):
        return self.thrust_duration

    def set_payload_weight(self, payload_weight):
        self.payload_weight = payload_weight
        self.__set_total_weight()

    def get_payload_weight(self):
        return self.payload_weight

    def __set_total_weight(self):
        self.total_weight = self.base_weight + self.payload_weight + self.fuel

    def get_total_weight(self):
        return self.total_weight
    
    def get_specific_impulse(self):
        return self.specific_impulse
    
    def get_thrust(self):
        return self.thrust
    
    def get_flow_rate(self):
        return self.flow_rate
    
    def get_drag_coefficiency(self):
        return self.drag_coefficiency
    
    def __repr__(self) -> str:
        return f"Rocket(base_weight={self.base_weight:_}, payload_weight={self.payload_weight:_}, fuel={self.fuel:_}, thrust_duration={self.thrust_duration:_}, total_weight={self.total_weight:_})"
