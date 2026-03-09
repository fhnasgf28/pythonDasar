
class StudyScheduler:
    def __init__(self):
        self.schedule = []
        self.subjects = ["Matematika", "Fisika", "Kimia", "Biologi", "Bahasa Inggris"]

    def add_study_session(self, subject, date, time):
        session = {
            "subject": subject,
            "date": date,
            "time": time
        }
        self.schedule.append(session)
        print(f"Added study session for {subject} on {date} at {time}")

    def view_schedule(self):
        if not self.schedule:
            print("No Study sessions scheduled.")
            return

        print("Study Schedule:")
        for i, session in enumerate(self.schedule, start=1):
            print(f"{i}. Subject: {session['subject']}, Date: {session['date']}, Time: {session['time']}")

    def remove_study_session(self, index):
        if 0 <= index < len(self.schedule):
            removed_session = self.schedule.pop(index)
            print(f"Removed study session for {removed_session['subject']} on {removed_session['date']} at {removed_session['time']}")
        else:
            print("Invalid session index.")

    def display_subjects(self):
        print("Available subjects:")
        for i, subject in enumerate(self.subjects, start=1):
            print(f"{i}. {subject}")

def main():
    scheduler = StudyScheduler()

    while True:
        print("\nStudy Scheduler Menu:")
        print("1. Add Study Session")
        print("2. View Schedule")
        print("3. Remove Study Session")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            scheduler.display_subjects()
            subject_index = int(input("Enter the subject index: "))
            if 0 <= subject_index < len(scheduler.subjects):
                subject = scheduler.subjects[subject_index]
                date = input("Enter the date (YYYY-MM-DD): ")
                time = input("Enter the time (HH:MM): ")
                scheduler.add_study_session(subject, date, time)
            else:
                print("Invalid subject index.")

        elif choice == '2':
            scheduler.view_schedule()

        elif choice == '3':
            scheduler.view_schedule()
            session_index = int(input("Enter the session index to remove: ")) - 1
            scheduler.remove_study_session(session_index)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()