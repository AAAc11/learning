from .errors import InvalidAgeError

def load_students(filepath):
    students = []
    try:
        with open(filepath,"r",encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        name, age_str = [x.strip() for x in line.split(',')]
                        students.append({"name": name, "age": int(age_str)})
                    except ValueError:
                        print("Error")
            return students
    except FileNotFoundError:
        print("No file found")
        return students

def save_students(filepath, students):
    with open(filepath,"w",encoding="utf-8") as f:
        for student in students:
            f.write(f"{student['name']}, {student['age']}\n")

def add_student(students, name, age):
    if 5 > age or age > 120:
        raise InvalidAgeError(age)

    student={"name": name, "age": age}
    students.append(student)
    return students

def get_older_than(students,threshold):
    return [x["name"] for x in students if x["age"] > threshold]

def find_duplicate(students):
    students_tuples = [tuple(sorted(student.items())) for student in students]
    return len(students_tuples)!= len(set(students_tuples))

def sum_scores(*scores):
    total = 0
    for score in scores:
        total += score
    return total
