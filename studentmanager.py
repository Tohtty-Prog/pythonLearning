import json
import os
class Course:
    def __init__(self,name,code):
        self.name = name
        self.code = code

class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def add_course(self,course):
        self.courses.append(course)

    def show_courses(self):
        if not self.courses:
            print("Student has no courses")
            return

        for course in self.courses:
            print(f"- {course.name} ({course.code})")

class StudentManager:
    def __init__(self, filename = "data.json"):
        self.filename = filename
        self.students = []
        self.courses = []
        self.check_file()
        self.load_data()

    def add_student(self, name, student_id):
        student = Student(name,student_id)
        self.students.append(student)

    def add_course(self,name,code):
        course = Course(name,code)
        self.courses.append(course)

    def find_student(self,student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def find_course(self,code):
        for course in self.courses:
            if course.code == code:
                return course
        return None
    
    def enroll_student(self,student_id,course_code):
        student = self.find_student(student_id)
        course = self.find_course(course_code)
        if student and course:
            student.add_course(course)
        else:
            print("Student or course not found")

    def show_students(self):
        if not self.students:
            print("No students found")
            return
        for student in self.students:
            print(student.name, student.student_id)


    def show_courses(self):
        if not self.courses:
            print("No courses found")
            return
        for course in self.courses:
            print(course.name, course.code)

    def show_student_info(self,student_id):
        student = self.find_student(student_id)
        if not student:
            print("Student not found")
            return
        print(f"Student Name: {student.name}\n Student_Id: {student.student_id}")
        student.show_courses()

    def check_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump({"students": []}, f, indent=4)
        else:
            pass

    def save_data(self):
        data = {
            "students": []
        }
        for student in self.students:
            student_data = {
                "name": student.name,
                "student_id": student.student_id,
                "courses": [
                    {"name": course.name, "code": course.code}
                    for course in student.courses
                ]
            }
            data["students"].append(student_data)

        with open(self.filename, "w") as f:
            json.dump(data,f,indent=4)

    def load_data(self):
        self.students = []
        self.courses = []
        data = {
            "students": []
        }
        with open(self.filename, 'r') as f:
            data = json.load(f)
            for student_data in data["students"]:
                student = Student(student_data["name"], student_data["student_id"])
                
                for course_data in student_data["courses"]:
                    course = Course(course_data["name"],course_data["code"])
                    student.add_course(course)
                    if not self.find_course(course.code):
                        self.courses.append(course)
                self.students.append(student)


def main():
    manager = StudentManager()
    while True:
        print("\n1. Add Student")
        print("2. Add course")
        print("3. Enroll student to course")
        print("4. Show students")
        print("5. Show courses")
        print("6. show student info: ")
        print("7. Save student data")
        print("8. Load student data")
        print("9. Exit")
        choice = input("Choose: ")
        if choice == '1':
            name = input("Student name: ")
            student_id = input("Student Id: ")
            manager.add_student(name,student_id)
        elif choice == '2':
            course = input("Course name: ")
            code = input("Course code: ")
            manager.add_course(course,code)
        elif choice == '3':
            student_id = input("Student ID: ")
            course_code = input("Course Code: ")
            manager.enroll_student(student_id,course_code)
        elif choice == '4':
            manager.show_students()
        elif choice == '5':
            manager.show_courses()
        elif choice == '6':
            student_id = input("Enter the students id: ")
            manager.show_student_info(student_id)
        elif choice == '7':
            manager.save_data()
        elif choice == '8':
            manager.load_data()
        elif choice == "9":
            print("Good bye")
            manager.save_data()
            break
        else: 
            print("Unknown choice")

if __name__ == "__main__":
    main()


