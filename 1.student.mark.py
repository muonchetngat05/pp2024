students = []
courses = []
marks = {}

def add_students():
    count = int(input("Enter the number of students to add: "))
    for i in range(count):
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Date of Birth: ")
        students.append((sid, name, dob))
        
def remove_students(students):
    if not students:
        print("Invalid")
    else:
        list_students()
        id = input("Enter the Student ID to remove: ")
        for student in students:
            if students[0] == id:
                students.remove(student)              
                print("Student has been removed.")
                break
        else:
            print("Invalid Student ID.")

def list_students():
    if not students:
        print("Invalid")
    else:
        print("\nList of Students:")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, DOB: {student[2]}")
    print("------")

def add_courses():
    count = int(input("Enter the number of courses to add: "))
    for j in range(count):
        cid = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        courses.append((cid, name))

def list_courses():
    if not courses:
        print("Invalid")
    else:
        print("\nList of Courses:")
        for course in courses:
            print(f"ID: {course[0]}, Name: {course[1]}")
    print("------")

def add_marks():
    if not students or not courses:
        print("Invalid")
    else:
        list_courses()
        course_id = input("Enter the Course ID to input marks: ")
        if course_id not in [course[0] for course in courses]:
            print("Invalid Course ID.")
        else:
            for student in students:
                mark = float(input(f"Enter the mark for {student[1]} (ID: {student[0]}): "))
                marks[(student[0], course_id)] = mark
            print("Marks have been successfully recorded.")

def view_marks():
    if not marks:
        print("Invalid")
    else:
        list_courses()
        course_id = input("Enter the Course ID to view marks: ")
        if course_id not in [course[0] for course in courses]:
            print("Invalid Course ID.")
        else:
            print(f"\nMarks for Course ID: {course_id}")
            for student in students:
                mark = marks.get((student[0], course_id), "No marks recorded")
                print(f"{student[1]} (ID: {student[0]}): {mark}")

def main_menu():
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
            add_students()
        elif choice == 2:
            remove_students(students)    
        elif choice == 3:
            list_students()
        elif choice == 4:
            add_courses()
        elif choice == 5:
            list_courses()
        elif choice == 6:
            add_marks()
        elif choice == 7:
            view_marks()
        elif choice == 8:
            print("Exited!")
            break
        else:
            print("Invalid choice!")

main_menu()
