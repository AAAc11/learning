users = {"Aga": 21, "Paweł": 18, "Ola": 17}

result =  {name: age*1.23 for name,age in users.items()}

print(result)