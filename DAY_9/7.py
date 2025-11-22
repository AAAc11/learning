"""
Polecenie:
Mapowanie z warunkiem: Użyj map i lambda, aby zamienić listę
liczb na stringi: 'Duża' jeśli liczba jest >= 10, a 'Mała' jeśli jest < 10.
"""

list_of_numbers = [12, 5, 15, 8, 20]
list_of_strings = list(map(lambda x: "Duża" if x >=10 else "Mała",list_of_numbers))

print(list_of_strings)