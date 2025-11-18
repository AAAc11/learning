class AgeError(Exception):
    pass

wiek=int(input("Podaj wiek: "))
if wiek<0:
    raise AgeError(f"Nie istniejesz")
else:
    print(f"masz {wiek} lat")