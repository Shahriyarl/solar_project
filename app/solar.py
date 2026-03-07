import math
import random

def solar_irradiance(hour):
    """
    Hesablayır günəş radiasiyasını saat üzrə (0-24)
    """
    max_irradiance = 1000  # W/m²
    value = max_irradiance * math.sin(math.pi * hour / 24)
    return max(value, 0)

def solar_panel_power(irradiance):
    """
    Hesablayır paneldən alınan DC gücü
    """
    panel_area = 10  # m²
    efficiency = 0.20  # 20%
    power = irradiance * panel_area * efficiency
    return power

class SolarSystem:
    def __init__(self):
        self.solar_power = 0
        self.battery_level = 50
        self.load = "ON"

    def update(self, hour):
        """
        Günün saatına görə sistem statusunu yeniləyir
        """
        irradiance = solar_irradiance(hour)
        power = solar_panel_power(irradiance)
        cloud = random.uniform(0.7, 1.0)  # bulud effekti
        self.solar_power = round(power * cloud, 2)

        # Batareya balansı
        if self.solar_power > 500:
            self.battery_level += 2
        else:
            self.battery_level -= 1

        self.battery_level = max(0, min(100, self.battery_level))

    def get_status(self):
        """
        JSON formatında məlumat qaytarır
        """
        return {
            "solar_power": self.solar_power,
            "battery": self.battery_level,
            "load": self.load
        }