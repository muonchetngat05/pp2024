class Student:
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def add_students(self):
        count = int(input("Enter the number of students to add: "))
        for i in range(count):
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            dob = input("Enter Date of Birth: ")
            print("------")
            self.students.append(Student(sid, name, dob))
        self.main_menu()

    def remove_student(self):
        if not self.students:
            print("No students available to remove.")
        else:
            sid_to_remove = input("Enter the ID of the student to remove: ")
            self.students = [s for s in self.students if s.sid != sid_to_remove]
            print("Student removed successfully.")
        self.main_menu()

    def list_students(self):
        if not self.students:
            print("No students have been added.")
        else:
            print("\nList of Students:")
            for student in self.students:
                print(f"ID: {student.sid}, Name: {student.name}, DOB: {student.dob}")
        print("------")
        self.main_menu()

    def add_courses(self):
        count = int(input("Enter the number of courses to add: "))
        for _ in range(count):
            cid = input("Enter Course ID: ")
            name = input("Enter Course Name: ")
            print("------")
            self.courses.append(Course(cid, name))
        self.main_menu()

    def list_courses(self):
        if not self.courses:
            print("No courses have been added.")
        else:
            print("\nList of Courses:")
            for course in self.courses:
                print(f"ID: {course.cid}, Name: {course.name}")
        print("------")
        self.main_menu()

    def add_marks(self):
        if not self.students or not self.courses:
            print("Please add both students and courses before entering marks.")
        else:
            self.list_courses()
            course_id = input("Enter the Course ID to input marks: ")
            if course_id not in [course.cid for course in self.courses]:
                print("Invalid Course ID.")
            else:
                for student in self.students:
                    mark = float(input(f"Enter the mark for {student.name} (ID: {student.sid}): "))
                    self.marks.append(Mark(student, course_id, mark))
                print("Marks have been successfully recorded.")
        self.main_menu()

    def view_marks(self):
        if not self.marks:
            print("No marks have been recorded.")
        else:
            self.list_courses()
            course_id = input("Enter the Course ID to view marks: ")
            if course_id not in [course.cid for course in self.courses]:
                print("Invalid Course ID.")
            else:
                print(f"\nMarks for Course ID: {course_id}")
                for mark in self.marks:
                    if mark.course == course_id:
                        print(f"{mark.student.name} (ID: {mark.student.sid}): {mark.mark}")
        self.main_menu()

    def process_choice(self, option):
        if option == 1:
            self.add_students()
        elif option == 2:
            self.remove_student()
        elif option == 3:
            self.list_students()
        elif option == 4:
            self.add_courses()
        elif option == 5:
            self.list_courses()
        elif option == 6:
            self.add_marks()
        elif option == 7:
            self.view_marks()
        elif option == 8:
            print("Program terminated. Goodbye!")
        else:
            print("Invalid choice. Please select a valid option.")
            self.main_menu()

    def main_menu(self):
        print("\nMAIN MENU")
        print("1. Add Students")
        print("2. Remove a Student")
        print("3. View Students")
        print("4. Add Courses")
        print("5. View Courses")
        print("6. Input Marks")
        print("7. View Marks")
        print("8. Exit")
        choice = int(input("Select an option: "))
        self.process_choice(choice)

if __name__ == "__main__":
    school = School()
    school.main_menu()