from .analyzer import file_analyzer
from datetime import date

class FileReport:
    def __init__(self, file_name):
        self.file_name = file_name
        (self.line_counter,
        self.word_counter,
        self.unique_words,
        self.empty_line_counter) = file_analyzer(file_name)

    def saving_report(self):
        with open(f"{self.file_name}report.txt",'w', encoding='utf-8') as f:
            f.writelines(f"Analysis from {date.today()}\n")
            f.writelines(f"File title: {self.file_name}\n")
            f.writelines(f"Number of lines: {self.line_counter}\n")
            f.writelines(f"Number of words: {self.word_counter}\n")
            f.writelines(f"Number of unique words: {self.unique_words}\n")
            f.writelines(f"Number of empty lines: {self.empty_line_counter}\n")