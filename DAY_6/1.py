with open("teoria.txt","r",encoding="utf-8") as f:

    content = f.readlines()

lengths = [len(line) for line in content]

print(f"liczba lini w calym pliku: {len(content)}")
print(lengths)