with open("numbers.txt", "w",encoding="utf-8") as f:
    for x in range(0,101):
        f.writelines(str(x)+"\n")