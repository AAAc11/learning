"""
Masz listę słów. Użyj filter i funkcji lambda, aby wybrać tylko te słowa, które mają więcej niż 5 liter.
"""

slowa = ["kot", "pies", "programowanie", "Python", "dom"]

more_than_five = lambda x: len(x) > 5

words_longer_than_five = list(filter(more_than_five, slowa))

print(words_longer_than_five)