from app.solar import SolarSystem

system = SolarSystem()
hour = 6

def system_step():
    """
    Hər çağırışda system update edir və JSON qaytarır
    """
    global hour
    system.update(hour)
    data = system.get_status()
    current_hour = hour
    hour += 1
    if hour > 18:
        hour = 6  # simulyasiya 6-dan 18-ə qədər

    return {
        "hour": current_hour,
        "solar_power": data["solar_power"],
        "battery": data["battery"],
        "load": data["load"]
    }

def get_system_status():
    """
    Sadəcə status qaytarır, hour artırılır
    """
    global hour
    system.update(hour)
    data = system.get_status()
    current_hour = hour
    hour += 1
    if hour > 18:
        hour = 6
    return {
        "hour": current_hour,
        **data
    }

def control_load(battery_percentage):
    """
    Batareya səviyyəsinə görə yükü idarə edir
    """
    if battery_percentage < 20:
        return 0  # yük söndürülür
    return 50  # 50W yük aktiv