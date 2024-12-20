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
            self.students.append((sid, name, dob))
        
    def remove_students(self):
        if not self.students:
            print("Invalid")
        else:
            self.list_students()
            id = input("Enter the Student ID to remove: ")
            for student in self.students:
                if student[0] == id:
                    self.students.remove(student)              
                    print("Student has been removed.")
                    break
            else:
                print("Invalid Student ID.")

    def list_students(self):
        if not self.students:
            print("Invalid")
        else:
            print("\nList of Students:")
            for student in self.students:
                print(f"ID: {student[0]}, Name: {student[1]}, DOB: {student[2]}")
        print("------")

    def add_courses(self):
        count = int(input("Enter the number of courses to add: "))
        for j in range(count):
            cid = input("Enter Course ID: ")
            name = input("Enter Course Name: ")
            self.courses.append((cid, name))

    def list_courses(self):
        if not self.courses:
            print("Invalid")
        else:
            print("\nList of Courses:")
            for course in self.courses:
                print(f"ID: {course[0]}, Name: {course[1]}")
        print("------")

    def add_marks(self):
        if not self.students or not self.courses:
            print("Invalid")
        else:
            self.list_courses()
            course_id = input("Enter the Course ID to input marks: ")
            if course_id not in [course[0] for course in self.courses]:
                print("Invalid Course ID.")
            else:
                for student in self.students:
                    mark = float(input(f"Enter the mark for {student[1]} (ID: {student[0]}): "))
                    self.marks.append((student[0], course_id, mark))
                print("Marks have been successfully recorded.")

    def view_marks(self):
        if not self.marks:
            print("Invalid")
        else:
            self.list_courses()
            course_id = input("Enter the Course ID to view marks: ")
            if course_id not in [course[0] for course in self.courses]:
                print("Invalid Course ID.")
            else:
                print(f"\nMarks for Course ID: {course_id}")
                for student in self.students:
                    mark = next((m[2] for m in self.marks if m[0] == student[0] and m[1] == course_id), "No marks recorded")
                    print(f"{student[1]} (ID: {student[0]}): {mark}")

    def main_menu(self):
        while True:
            print("\nMAIN MENU")
            print("1. Add Students")
            print("2. Remove students")
            print("3. View Students")
            print("4. Add Courses")
            print("5. View Courses")
            print("6. Input Marks")
            print("7. View Marks")
            print("8. Exit")
            choice = int(input("Select an option: "))
            if choice == 1:
                self.add_students()
            elif choice == 2:
                self.remove_students()    
            elif choice == 3:
                self.list_students()
            elif choice == 4:
                self.add_courses()
            elif choice == 5:
                self.list_courses()
            elif choice == 6:
                self.add_marks()
            elif choice == 7:
                self.view_marks()
            elif choice == 8:
                print("Exited!")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    school = School()
    school.main_menu()
