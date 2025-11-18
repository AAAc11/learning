studenci = [
    {'imie': 'Anna', 'wiek': 21, 'srednia': 4.5},
    {'imie': 'Tomasz', 'wiek': 23, 'srednia': 3.9},
    {'imie': 'Ewa', 'wiek': 21, 'srednia': 4.8},
    {'imie': 'Piotr', 'wiek': 22, 'srednia': 4.5},
]

sortuj_studentow=sorted(studenci, key = lambda s: (-s['srednia'], s['wiek']))

print([s['imie'] for s in sortuj_studentow])