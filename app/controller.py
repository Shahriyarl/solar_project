def control_load(battery_percentage):
    if battery_percentage < 20:
        return 0  # yük söndürülür
    return 50  # 50W yük aktiv