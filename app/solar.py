import math
import random 

def get_solar_power(hour: int):
    if 6 <= hour <= 18:
        base = 100 * math.sin((hour - 6) * math.pi / 12)
        cloud_effect = random.uniform(0.7, 1.0)
        return round(base * cloud_effect, 2)
    return 0
            