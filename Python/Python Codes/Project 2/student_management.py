print("Python Student Management System")
import json
import os

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"\nStudent ID: {self.student_id}")
        print(f"Name      : {self.name}")
        print(f"Age       : {self.age}")
        print(f"Grade     : {self.grade}")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        return Student(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            grade=data["grade"]
        )


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.file_name = "students.json"
        self.load_from_file()

    def add_student(self):
        print("\n--- Add New Student ---")
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Name: ").strip()
        age = input("Enter Age: ").strip()
        grade = input("Enter Grade: ").strip()

        
        if any(student.student_id == student_id for student in self.students):
            print(" Student with this ID already exists!")
            return

        student = Student(student_id, name, age, grade)
        self.students.append(student)
        self.save_to_file()
        print(" Student added and saved successfully!")

    def view_student(self):
        print("\n--- View Student Details ---")
        student_id = input("Enter Student ID: ").strip()
        found = False
        for student in self.students:
            if student.student_id == student_id:
                student.display_info()
                found = True
                break
        if not found:
            print(" Student not found.")

    def display_all(self):
        print("\n--- All Students ---")
        if not self.students:
            print("No students to display.")
        else:
            for student in self.students:
                student.display_info()

    def save_to_file(self):
        data = [student.to_dict() for student in self.students]
        with open("Students.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        if os.path.exists("Students.json"):
            with open("Students.json", "r") as f:
                try:
                    data = json.load(f)
                    self.students = [Student.from_dict(item) for item in data]
                except json.JSONDecodeError:
                    self.students = []
        else:
            self.students = []

    @staticmethod
    def menu():
        print("\n======= Student Management System =======")
        print("1. Add Student")
        print("2. View Student by ID")
        print("3. Display All Students")
        print("4. Exit")


def main():
    system = StudentManagementSystem()

    while True:
        StudentManagementSystem.menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.view_student()
        elif choice == '3':
            system.display_all()
        elif choice == '4':
            print(" Exiting... Thank you for using the system!")
            break
        else:
            print(" Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
