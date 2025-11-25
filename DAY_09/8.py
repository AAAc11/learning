"""
Użyj filter i lambda, aby wybrać z listy słów tylko te,
które mają więcej niż 5 znaków.
"""

list_of_words = ['python', 'java', 'cplusplus', 'swift', 'go']
longer_than_5 = list(filter(lambda x: len(x) > 5, list_of_words))

print(longer_than_5)

