slowa = ["Python", "Java", "Go", "C++", "Rust", "JavaScript"]

result=[x.capitalize() for x in slowa if len(x)>=4]

print(result)