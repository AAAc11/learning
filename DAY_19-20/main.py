import sys
from typing import NoReturn
from file_analyzer.report import FileReport
from file_analyzer.logger import log_action


def main() -> NoReturn:
    log_action("Program started")
    print("Starting")

    # 1. Interaktywne pobieranie nazwy pliku
    try:
        input_file_name = input("\nEnter file name: ")

        if not input_file_name.strip():
            print("\nNo name typed")
            sys.exit(1)

    except EOFError:
        print("\nError")
        log_action("Error: EOFError")
        sys.exit(1)

    try:
        # 2. Inicjalizacja i analiza
        print(f"\nAnalyzing: '{input_file_name}'...")

        report = FileReport(input_file_name)

        report.saving_report()

    except Exception as e:
        log_action(f"Error: {e}")
        sys.exit(1)

    print(f"\nCheck logs: {input_file_name}.txt")
    log_action("Program finished\n")


if __name__ == "__main__":
    main()