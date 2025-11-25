with open("numbers.txt","r",encoding="utf-8") as src, \
    open("reverse_numbers.txt","w",encoding="utf-8") as dst:
        content = src.readlines()
        dst.writelines(content[::-1])