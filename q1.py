import os


def add_course():
    course_code = input("Enter the course code: ")
    course_name = input("Enter the course name: ")
    credit_hour = input("Enter the credit hour: ")

    with open("course_info.txt", "a") as file:
        file.write(f"{course_code},{course_name},{credit_hour}\n")


def add_student():
    student_id = input("Enter the student ID: ")
    student_name = input("Enter the student name: ")
    program_code = input("Enter the program code: ")

    courses = []
    add_more_courses = True
    while add_more_courses:
        course_code = input("Enter the course code: ")
        course_score = input("Enter the course score: ")
        courses.append(f"{course_code}:{course_score}")

        choice = input("Do you want to add another course? (y/n): ")
        if choice.lower() != "y":
            add_more_courses = False

    with open("student_info.txt", "a") as file:
        file.write(f"{student_id},{student_name},{program_code},{','.join(courses)}\n")


def main():
    while True:
        print("Main Menu")
        print("Choose any of these options:")
        print("1. Add a course")
        print("2. Add a student")
        print("3. Add a teacher")
        print("4. List all students")
        print("5. List all teachers")
        print("6. Search for a student by their name or student ID")
        print("7. List the teachers and their courses for a student")
        print("8. Show the GPA of a course")
        print("Enter zero to exit the program.")
        choice = input("Enter your choice: ")

        if choice == "0":
            break
        elif choice == "1":
            add_course()

        elif choice == "2":
            add_student()
        '''
        elif choice == "3":
            add_teacher()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_teachers()
        elif choice == "6":
            search_student()
        elif choice == "7":
            list_teacher_courses()
        elif choice == "8":
            show_course_gpa()
        else:
            print("Invalid choice. Please try again.")
            print()
        '''

for file_name in ["student_info.txt", "course_info.txt", "teacher_info.txt"]:
    if not os.path.exists(file_name):
        open(file_name, "w").close()


main()