#Sarah, Vinni, Breanna
class Ambulance:
    """Represents an emergency vehicle.
    Atributes color, traffic, patient, speed."""

truck = Ambulance()
truck.color= "red"
truck.traffic= 45
truck.patient= 1
truck.speed= 60

import math
def emergency_speed(amb):
    if truck.patient > 0:
        s=2.3*(truck.patient-0.5)*truck.traffic+30*(truck.patient-2.143)
        return s
    else:
        return truck.traffic


print (emergency_speed(truck))
