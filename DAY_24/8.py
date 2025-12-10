"""
Masz listę napisów. Użyj reduce i funkcji lambda, aby połączyć (skonkatenować)
wszystkie napisy w jeden ciąg, dodając spację pomiędzy nimi.
"""
from functools import reduce

fragmenty = ["Uczę", "się", "funkcji", "wyższego", "rzędu"]

connected = reduce(lambda a, b: a + " " + b, fragmenty)

print(connected)