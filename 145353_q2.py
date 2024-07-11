# 12345_q2.py
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f"Student Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, student_name):
        for student in self.students:
            if student.name == student_name:
                if student.grades:
                    average = sum(student.grades.values()) / len(student.grades)
                    print(f"Average grade for {student.name}: {average}")
                else:
                    print(f"No grades available for {student.name}")
                return
        print(f"Student named {student_name} not found.")

    def get_class_average(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count:
            print(f"Class average for {subject}: {total / count}")
        else:
            print(f"No grades available for {subject}")

def main():
    classroom = Classroom()

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Get Student Average")
        print("4. Get Class Average for a Subject")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter student's name: ")
            student = Student(name)
            while True:
                subject = input("Enter subject (or type 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                grade = float(input(f"Enter grade for {subject}: "))
                student.add_grade(subject, grade)
            classroom.add_student(student)
        elif choice == 2:
            classroom.display_students()
        elif choice == 3:
            name = input("Enter student's name to get average: ")
            classroom.get_student_average(name)
        elif choice == 4:
            subject = input("Enter subject to get class average: ")
            classroom.get_class_average(subject)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
