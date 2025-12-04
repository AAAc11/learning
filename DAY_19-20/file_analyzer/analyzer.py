from .reader import file_reader
from collections import Counter
from typing import Counter as CounterType, Tuple, List

def file_analyzer(file_name):
    line_counter = 0
    empty_line_counter = 0
    word_counter = Counter()

    context = file_reader(file_name)

    for line in context:
        line_counter += 1

        if not line.strip():
            empty_line_counter += 1
            continue

        words = line.lower().strip().split()

        cleaned_words = [word.strip(".,!?:;\"'()[]{}") for word in words if word.strip()]
        word_counter.update(cleaned_words)

    unique_word_count = len(word_counter)

    return line_counter, word_counter, unique_word_count, empty_line_counter