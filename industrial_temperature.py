def trigger_alarm(temperatures, threshold=80):
    alarms = []
    for sensor_name, reading in temperatures.items():
        if reading > threshold:
            alarms.append(sensor_name)          
    return alarms
temp_data_1 = {
    "sensor_1": 85.5,
    "sensor_2": 90.2,
    "sensor_3": 78.8,
    "sensor_4": 92.3
}
print(f"Alarma con límite 88: {trigger_alarm(temp_data_1, 88)}")
temp_data_2 = {
    "sensor_A": 79.0,
    "sensor_B": 81.2,
    "sensor_C": 75.4,
    "sensor_D": 85.7
}
print(f"Alarma con límite por defecto: {trigger_alarm(temp_data_2)}")