class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.total_marks = sum(marks)

    def calculate_total(self):
        self.total_marks = sum(self.marks)

    def check_result(self, passing_marks):
        self.calculate_total()
        if self.total_marks >= passing_marks:
            result = "Pass"
        else:
            result = "Fail"
        print(f"student: {self.name}, Roll Number: {self.roll_number}, Result: {result}")


# Create a student object
student1 = Student("Bob", 101, [79, 90, 65, 34])

# calculate total_marks
student1.calculate_total()

# check result with passing marks
student1.check_result(67)
