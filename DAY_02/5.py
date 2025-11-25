def zlacz_teksty(*slowa, seprarator=" "):
    slowa=slowa[0]
    ciag=''
    for slowo in slowa:
        ciag+=slowo+seprarator
    return ciag

def main():
    slowa=["widelec", "lyzka", "noz"]
    print(zlacz_teksty(slowa,seprarator=";"))
main()