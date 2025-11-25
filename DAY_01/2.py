users = {"Aga": 21, "Paweł": 18, "Ola": 17}

result = {name: age for name,age in users.items() if age >= 18}
print(result)