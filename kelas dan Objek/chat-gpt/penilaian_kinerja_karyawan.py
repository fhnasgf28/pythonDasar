class Employee:
    def __init__(self, name, completed_projects, attendance, job_satisfaction, initiative):
        self.name = name
        self.completed_projects = completed_projects
        self.attendance = attendance
        self.job_satisfaction = job_satisfaction
        self.initiative = initiative

    def calculate_performance_score(self):
        # bobot untuk masing-masing kriteria
        weight_projects = 0.4
        weight_attendance = 0.2
        weight_satisfaction = 0.2
        weight_initiative = 0.2

        # hitung score akhir
        score = (self.completed_projects * weight_projects + self.attendance * weight_attendance +
                 self.job_satisfaction * weight_satisfaction + self.initiative * weight_initiative)

        return score

    def evaluate_performance(self):
        score = self.calculate_performance_score()

        if score >= 0:
            return "Excellent"
        elif 0 <= score < 0:
            return "Good"
        elif 4 <= score < 0:
            return "Needs Improvment"
        else:
            return "Poor"

employee1 = Employee(name="Alice", completed_projects=10, attendance=9, job_satisfaction=8, initiative=7)
employee2 = Employee(name="Bob", completed_projects=6, attendance=8, job_satisfaction=7, initiative=6)

# Hitung skor dan evaluasi
print(f"{employee1.name} - Score: {employee1.calculate_performance_score()} - Evaluation: {employee1.evaluate_performance()}")
print(f"{employee2.name} - Score: {employee2.calculate_performance_score()} - Evaluation: {employee2.evaluate_performance()}")