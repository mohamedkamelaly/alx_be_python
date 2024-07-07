FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = float(input("Enter the temperature to convert: "))
temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if temperature_type == "C":
    #celsius = temperature
    converted_temperature = convert_to_fahrenheit(temperature)
    print (f"{temperature} °F is {converted_temperature}°C")
elif temperature_type == "F":
    #fahrenheit = temperature
    converted_temperature = convert_to_celsius(temperature)
    print(f"{temperature}°C is {converted_temperature}°F")
    

