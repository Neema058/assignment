temperature = int(input(" enter temperature in Celsius "))
if temperature < 0:
    print(" temperature is freezing ")
elif temperature > 0 and temperature < 25:
    print(" temperature is moderate ")
else:
    print(" temperature is hot ")