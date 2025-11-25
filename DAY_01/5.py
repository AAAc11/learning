from itertools import count

zakupy = ['jajka', 'mleko', 'chleb', 'jajka', 'masło', 'mleko', 'jajka']

dict1= {name: zakupy.count(name) for name in set(zakupy)}

print(dict1)
