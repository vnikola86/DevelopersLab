def determine_water_state(temperature):

    if temperature > 0 and temperature < 100:
        return "tečno"
    elif temperature <= 0:
        return "čvrsto"
    elif temperature >= 100:
        return "gasovito"

water_temperature = int(input("Unesite temperaturu vode: "))

water_state = determine_water_state(water_temperature)
print(f"Agregatno stanje vode temperature {water_temperature}°C je: {water_state}.")
