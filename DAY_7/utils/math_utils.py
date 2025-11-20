from . import file_utils as fu

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def calculate_and_save(a, b, operation, filename):
    match operation:
        case "add":
            result = add(a,b)
            fu.write_text_file(filename,f"Result: {result}")
        case "subtract":
            result = subtract(a,b)
            fu.write_text_file(filename, f"Result: {result}")
        case "multiply":
            result = multiply(a,b)
            fu.write_text_file(filename, f"Result: {result}")
