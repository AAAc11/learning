"""
Polecenie:
Napisz własną funkcję filter jako ćwiczenie
"""

def my_filter(function, object):
    correct_answers = []
    for element in object:
        if function(element):
            correct_answers.append(element)
    return correct_answers