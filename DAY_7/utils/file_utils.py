def read_text(filename):
    with open(filename,"r",encoding="utf-8") as f:
        content = f.read()
    return content

def write_text_file(filename, content):
    with open(filename,"w",encoding="utf-8") as f:
        f.write(content)
