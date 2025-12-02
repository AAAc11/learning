from reader import file_reader
from collections import Counter

def file_analyzer(file_name: str):
    line_counter = 0
    empty_line_counter = 0
    word_counter = 0
    unique_words = []
    context = file_reader(file_name)
    for line in context:
        if line == '':
            empty_line_counter +=1
            break
        line_counter +=1

        words = line.lower().split()
        word_counter = Counter(words)

        unique_words = [word for word, count in word_counter.items() if count == 1]

    return line_counter, word_counter, unique_words, empty_line_counter