
 from student import Student
from student_manager import StudentManager
from storage import load_students, save_students
manager = StudentManager()
# Load students from students.json
manager.students = load_students("students.json", Student)
while True:
 print("\n===== Student Management System =====")
 print("1. Add Student")
 print("2. View Students")
 print("3. Find Student")
 print("4. Update Student")
 print("5. Delete Student")
 print("6. Exit")
 choice = input("Enter your choice: ")
 if choice == "1":
 # Read student details
 name = input("Enter student name: ")
 age = int(input("Enter student age: "))
 python = float(input("Enter Python marks: "))
 mathematics = float(input("Enter Mathematics marks: "))
 communication = float(input("Enter Communication marks: "))
 # Create a Student object
 student = Student(
 name,
 age,
 python,
 mathematics,
 communication
 )
 # Add the student to the manager
 manager.add_student(student)
