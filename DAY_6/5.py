def find_lines_w_words(src,word):
    with open(src,"r",encoding="utf-8") as src, \
        open("lines_w_words","w",encoding="utf-8") as dst:
        for line in src:
            if word in line:
                dst.write(line)


def main():
    find_lines_w_words("teoria.txt","tylko")

main()