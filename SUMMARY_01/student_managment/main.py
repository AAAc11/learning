import services.student_service as ss
from services.errors import InvalidAgeError


DATA_FILE = "data/students.txt"

students = ss.load_students(DATA_FILE)
try:
    ss.add_student(students,"Mariusz", 11)
    ss.add_student(students,"Mikołaj", 3) #incorrect
except InvalidAgeError:
    print(InvalidAgeError)


older = ss.get_older_than(students,20)
print(f"Older than 20: {older}")

print(f"Duplicates: {ss.find_duplicate(students)}")

print(f"Actual students list: {students}")

ss.save_students(DATA_FILE, students)



