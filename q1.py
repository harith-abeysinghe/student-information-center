import os

def add_course():
    course_code = input("Enter the course code: ")

    with open("course_info.txt", "r") as file:
        course_records = file.readlines()
        for record in course_records:
            existing_course_code = record.strip().split(",")[0]
            if existing_course_code == course_code:
                print("This course code exists in our database.")
                return

    course_name = input("Enter the course name: ")

    valid_credit_hour = False
    while not valid_credit_hour:
        credit_hour = input("How many credit hours does this course have? ")
        try:
            credit_hour = int(credit_hour)
            if 1 <= credit_hour <= 5:
                valid_credit_hour = True
            else:
                print("The credit hour for each course should be an integer between 1 and 5 inclusive.")
        except ValueError:
            print("The credit hour for each course should be an integer between 1 and 5 inclusive.")

    with open("course_info.txt", "a") as file:
        file.write(f"{course_code},{course_name},{credit_hour}\n")

    print("Course added successfully.")


def add_student():
    student_id = input("Enter the student ID: ")

    with open("student_info.txt", "r") as file:
        student_records = file.readlines()
        for record in student_records:
            existing_student_id = record.strip().split(",")[0]
            if existing_student_id == student_id:
                print("This student ID exists in our database.")
                return

    student_name = input("Enter the student name: ")
    program_code = input("Enter the program code: ")

    valid_input = False
    while not valid_input:
        try:
            no_of_courses = int(input("How many courses does this student have? "))
            if no_of_courses < 1 or no_of_courses > 5:
                print("You can enter a number between 1 to 5.")
            else:
                valid_input = True
        except ValueError:
            print("Number of courses should be an integer value.")

    courses = []
    for i in range(no_of_courses):
        course_code = input(f"Enter course code {i + 1}: ")

        # Check if the course code exists
        course_exists = False
        with open("course_info.txt", "r") as file:
            course_records = file.readlines()
            for record in course_records:
                existing_course_code = record.strip().split(",")[0]
                if existing_course_code == course_code:
                    course_exists = True
                    break

        if not course_exists:
            print("This course does not exist in our database.")
            continue

        course_score = input("Enter the student's score for this course: ")
        courses.append(f"{course_code}:{course_score}")

    courses_data = ",".join(courses)

    with open("student_info.txt", "a") as file:
        file.write(f"{student_id},{student_name},{program_code},{courses_data}\n")

    print("Student added successfully.")


def add_teacher():
    staff_id = input("Enter the staff ID: ")

    # Check if the staff ID already exists
    with open("teacher_info.txt", "r") as file:
        teacher_records = file.readlines()
        for record in teacher_records:
            existing_staff_id = record.strip().split(",")[0]
            if existing_staff_id == staff_id:
                print("This teacher ID exists in our database.")
                return

    staff_name = input("Enter the teacher name: ")

    is_no_of_courses_valid = False
    while not is_no_of_courses_valid:
        no_of_courses = input("How many courses does this teacher teach? ")
        try:
            no_of_courses = int(no_of_courses)
            if 1 <= no_of_courses <= 5:
                is_no_of_courses_valid = True
            else:
                print("You can enter a number between 1 to 5.")
        except ValueError:
            print("Number of courses should be an integer value.")

    courses = []
    for i in range(no_of_courses):
        course_code = input(f"Enter course code {i + 1}: ")

        # Check if the course code already exists
        with open("course_info.txt", "r") as file:
            course_records = file.readlines()
            course_codes = [record.strip().split(",")[0] for record in course_records]
            if course_code in course_codes:
                print("This course has been entered before.")
                continue

        courses.append(course_code)

    # Append the teacher record to the file
    with open("teacher_info.txt", "a") as file:
        file.write(f"{staff_id},{staff_name},{','.join(courses)}\n")

    print("Teacher added successfully.")


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


add_teacher()
