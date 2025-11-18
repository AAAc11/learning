users = {"Aga": 21, "Paweł": 18, "Ola": 17}

sor=sorted(users.items(), key=lambda item:item[1])

print(sor)