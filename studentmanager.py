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
    def __init__(self):
        self.students = []
        self.courses = []

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

def main():
    manager = StudentManager()
    while True:
        print("\n1. Add Student")
        print("2. Add course")
        print("3. Enroll student to course")
        print("4. Show students")
        print("5. Show courses")
        print("6. show student info: ")
        print("7. Exit")
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
        elif choice == "7":
            print("Good bye")
            break
        else: 
            print("Unknown choice")

if __name__ == "__main__":
    main()


