"""
Masz listę temperatur w stopniach Fahrenheita. Użyj map i funkcji
lambda, aby przeliczyć każdą temperaturę na stopnie Celsjusza, używając wzoru:
C = (F - 32) * 5/9
"""

fahrenheity = [32, 68, 86, 104, 212]

fahrenheit_to_celsius = lambda x: (x-32) * 5 / 9
celsius_temperature = list(map(fahrenheit_to_celsius, fahrenheity))

print(celsius_temperature)
