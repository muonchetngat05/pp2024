students = []
courses = []
marks = {}

def add_students():
    count = int(input("Enter the number of students to add: "))
    for _ in range(count):
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Date of Birth: ")
        print("------")
        students.append({"id": sid, "name": name, "dob": dob})
    main_menu()

def remove_student():
    if not students:
        print("No students available to remove.")
    else:
        sid_to_remove = input("Enter the ID of the student to remove: ")
        students[:] = [s for s in students if s["id"] != sid_to_remove]
        print("Student removed successfully.")
    main_menu()

def list_students():
    if not students:
        print("No students have been added.")
    else:
        print("\nList of Students:")
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")
    print("------")
    main_menu()

def add_courses():
    count = int(input("Enter the number of courses to add: "))
    for _ in range(count):
        cid = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        print("------")
        courses.append({"id": cid, "name": name})
    main_menu()

def list_courses():
    if not courses:
        print("No courses have been added.")
    else:
        print("\nList of Courses:")
        for course in courses:
            print(f"ID: {course['id']}, Name: {course['name']}")
    print("------")
    main_menu()

def add_marks():
    if not students or not courses:
        print("Please add both students and courses before entering marks.")
    else:
        list_courses()
        course_id = input("Enter the Course ID to input marks: ")
        if course_id not in [course["id"] for course in courses]:
            print("Invalid Course ID.")
        else:
            for student in students:
                mark = float(input(f"Enter the mark for {student['name']} (ID: {student['id']}): "))
                marks[(student["id"], course_id)] = mark
            print("Marks have been successfully recorded.")
    main_menu()

def view_marks():
    if not marks:
        print("No marks have been recorded.")
    else:
        list_courses()
        course_id = input("Enter the Course ID to view marks: ")
        if course_id not in [course["id"] for course in courses]:
            print("Invalid Course ID.")
        else:
            print(f"\nMarks for Course ID: {course_id}")
            for student in students:
                mark = marks.get((student["id"], course_id), "No marks recorded")
                print(f"{student['name']} (ID: {student['id']}): {mark}")
    main_menu()

def process_choice(option):
    if option == 1:
        add_students()
    elif option == 2:
        remove_student()
    elif option == 3:
        list_students()
    elif option == 4:
        add_courses()
    elif option == 5:
        list_courses()
    elif option == 6:
        add_marks()
    elif option == 7:
        view_marks()
    elif option == 8:
        print("Program terminated. Goodbye!")
    else:
        print("Invalid choice. Please select a valid option.")
        main_menu()

def main_menu():
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
    process_choice(choice)

main_menu()
