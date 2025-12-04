
from typing import List

def file_reader(file_name: str) -> List[str]:
    try:
        with open(file_name,'r',encoding='utf-8') as f:
            context: List[str] = f.readlines()

        print(f"File {file_name} loaded correctly")
        return context

    except FileNotFoundError:
        print("No file found")
        print("No file found")
        return []
