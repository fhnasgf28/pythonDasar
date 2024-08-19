import json

# load the JSON data from the file
json_path = r'/mnt/7C7452557452126E/pythonDasar/latihan_Random/blackbox_ai/data_json/student.json'


def load_students():
    with open(json_path, 'r') as f:
        return json.load(f)


# save ths JSON data to the file
def save_students(students):
    with open(json_path, 'w') as f:
        json.dump(students, f, indent=4)


# add a new student to the database
def add_student(name, grade, subjects):
    students = load_students()
    new_student = {
        "id": len(students) + 1,
        "name": name,
        "grade": grade,
        "subjects": subjects
    }
    students.append(new_student)
    save_students(students)


# update a students grade level
def update_grade(student_id, new_grade):
    students = load_students()
    for student in students:
        if student["id"] == student_id:
            student["grade"] = new_grade
            break
    save_students(students)


# Remove a student from the database
def remove_student(student_id):
    students = load_students()
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            break
    save_students(students)


# list all students enrolled in a specific subject
def list_students_by_subject(subject):
    students = load_students()
    return [student for student in students if subject in student["subjects"]]


#calculate the average grade level of all students
def calculate_average_grade():
    students = load_students()
    total_grade = sum(student["grade"] for student in students)
    return total_grade / len(students)


# test the functions
add_student("Alice Johnson", 10, ["Math", "Science", "English"])
update_grade(2, 12)
remove_student(3)
print(list_students_by_subject("Math"))
print(calculate_average_grade())
