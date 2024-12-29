class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.classroom = None

    def assign_classroom(self, classroom):
        if self.classroom:
            raise ValueError(f"Student {self.name} is already assigned to a classroom.")
        classroom.add_student(self)

    def __str__(self):
        return f"Student {self.name} (ID: {self.student_id})"

class Classroom:
    def __init__(self, class_id, name):
        self.class_id = class_id
        self.name = name
        self.students = []

    def add_student(self, student):
        if student in self.students:
            raise ValueError(f"Student {student.name} is already in this classroom.")
        if student.classroom:
            raise ValueError(f"Student {student.name} is already assigned to another classroom.")
        self.students.append(student)
        student.classroom = self

    def list_students(self):
        print(f"Daftar siswa di kelas {self.name}:")
        if not self.students:
            print("Tidak ada siswa dalam kelas ini.")
        else:
            for student in self.students:
                print(f"- {student.name} (ID: {student.student_id})")

    def __str__(self):
        return f"Classroom {self.name} (ID: {self.class_id})"

# Contoh penggunaan
if __name__ == "__main__":
#     membuat objek student
    classroom1 = Classroom(1, "Class A")
    classroom2 = Classroom(2, "Class B")

    student1 = Student(1, "John")
    student2 = Student(2, "Jane")

    classroom1.add_student(student1)
    classroom1.add_student(student2)

    classroom1.list_students()
    classroom2.list_students()

# menambahkan siswa ke kelas
    print(f"\nMenambahkan siswa ke kelas:")
    student3 = Student(3, "Bob")
    classroom1.add_student(student3)
    classroom1.list_students()

# Mencoba menambahkan siswa ke kelas lain (harus gagal)
    try:
        print(f"Mencoba menambahkan {student1.name} ke {classroom2.name}")
        student1.assign_classroom(classroom2)
    except ValueError as e:
        print(e)

    # Menampilkan daftar siswa di kelas
    classroom1.list_students()
    classroom2.list_students()
