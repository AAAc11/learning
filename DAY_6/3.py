def copy_file(src,dest):
    with open(src,"r",encoding="utf-8") as s, \
    open(dest,"a",encoding="utf-8") as d:
        for line in s:
            d.write(line)

def main():
    copy_file("numbers.txt","nums1.txt")

main()
