import math
import random 

def get_solar_power(hour: int):
    if 6 <= hour <= 18:
        base = 100 * math.sin((hour - 6) * math.pi / 12)
        cloud_effect = random.uniform(0.7, 1.0)
        return round(base * cloud_effect, 2)
    return 0        



class SolarSystem:

    def __init__(self):
        self.solar_power = 0
        self.battery_level = 0
        self.load = ""

    def update(self):
        # Load random dəyişir
        if self.battery_level < 10:
            self.load = "OFF"
        else:
            self.load = "ON"

        # Günəş enerjisi random dəyişir
        self.solar_power = random.randint(0, 300)

        # Günəş zəifdirsə batareya işləyir
        if self.solar_power <= 10:

            if self.battery_level > 0:
                self.battery_level -= random.randint(1,3)

        # Günəş varsa batareya dolur
        else:

            if self.battery_level < 100:
                self.battery_level += random.randint(1,2)

        # limitlər
        if self.battery_level < 0:
            self.battery_level = 0

        if self.battery_level > 100:
            self.battery_level = 100


    def show_status(self):

        print("----- SOLAR SYSTEM -----")
        print(f"Solar Power: {self.solar_power} W")
        print(f"Battery Level: {self.battery_level} %")
        print(f"Load: {self.load}")
        print("------------------------\n")