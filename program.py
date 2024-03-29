'''
    Name:
    SID:
    Unikey:
'''
import os

def is_valid_student_id(student_id):
    return len(student_id) == 10


def is_valid_teacher_id(teacher_id):
    return len(teacher_id) == 7



def is_valid_program_code(program_code):
    return len(program_code) == 5


def is_valid_course_code(course_code):
    return len(course_code) == 6


def is_valid_name(name):
    return 1 <= len(name) <= 40 and name.isalpha()


def is_valid_score(score):
    try:
        score = float(score)
        return 0 <= score <= 100
    except ValueError:
        return False

def is_valid_credit_hour(credit_hour):
    try:
        credit_hour = int(credit_hour)
        if 1 <= credit_hour <= 5:
            return True
        else:
            return False
    except ValueError:
        return False


def add_course():
    course_code = input("Enter the course code: ")
    if not is_valid_course_code(course_code):
        print("The length of course codes entered should be 6.")
        return

    with open("course_info.txt", "r") as file:
        course_records = file.readlines()
        for record in course_records:
            existing_course_code = record.strip().split(",")[0]
            if existing_course_code == course_code:
                print("This course code exists in our database.")
                return

    course_name = input("Enter the course name: ")
    if not is_valid_name(course_name):
        print(
            "The length of the course name should be between 1 and 40 characters inclusive, and it should be alphabetic.")
        return

    valid_credit_hour = False
    while not valid_credit_hour:
        credit_hour = input("How many credit hours does this course have? ")
        if is_valid_credit_hour(credit_hour):
            valid_credit_hour = True
        else:
            print("The credit hour for each course should be an integer between 1 and 5 inclusive.")

    with open("course_info.txt", "a") as file:
        file.write(f"{course_code},{course_name},{credit_hour}\n")

    print("Course added successfully.")


def add_student():
    student_id = input("Enter the student ID: ")
    if not is_valid_student_id(student_id):
        print("The length of the student ID should be 10 characters.")
        return

    with open("student_info.txt", "r") as file:
        student_records = file.readlines()
        for record in student_records:
            existing_student_id = record.strip().split(",")[0]
            if existing_student_id == student_id:
                print("This student ID exists in our database.")
                return

    student_name = input("Enter the student name: ")
    if not is_valid_name(student_name):
        print("The length of the student name should be between 1 and 40 characters inclusive, and it should be alphabetic.")
        return
    program_code = input("Enter the program code: ")
    if not is_valid_program_code(program_code):
        print("The length of the program code entered should be 5.")
        return
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

        valid_score = False
        while not valid_score:
            course_score = input("Enter the student's score for this course: ")
            try:
                course_score = float(course_score)
                if 0 <= course_score <= 100:
                    valid_score = True
                else:
                    print("The score for each course should be in the range of 0 to 100.")
            except ValueError:
                print("Score should be a float value.")

        courses.append(f"{course_code}:{course_score}")

    courses_data = ",".join(courses)

    with open("student_info.txt", "a") as file:
        file.write(f"{student_id},{student_name},{program_code},{courses_data}\n")

    print("Student added successfully.")



def add_teacher():
    staff_id = input("Enter the staff ID: ")
    if not is_valid_teacher_id(staff_id):
        print("The length of the staff ID should be 7 characters.")
        return

    with open("teacher_info.txt", "r") as file:
        teacher_records = file.readlines()
        for record in teacher_records:
            existing_staff_id = record.strip().split(",")[0]
            if existing_staff_id == staff_id:
                print("This teacher ID exists in our database.")
                return

    staff_name = input("Enter the teacher name: ")
    if not is_valid_name(staff_name):
        print("The length of the teacher name should be between 1 and 40 characters inclusive, and it should be alphabetic.")
        return
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
        if not is_valid_course_code(course_code):
            print("The length of the course code entered should be 6.")
            return

        with open("course_info.txt", "r") as file:
            course_records = file.readlines()
            course_codes = [record.strip().split(",")[0] for record in course_records]
            if course_code in course_codes:
                print("This course has been entered before.")
                continue

        courses.append(course_code)

    with open("teacher_info.txt", "a") as file:
        file.write(f"{staff_id},{staff_name},{','.join(courses)}\n")

    print("Teacher added successfully.")


def list_students():
    with open("student_info.txt", "r") as file:
        for line in file:
            student_data = line.strip().split(",")
            student_id = student_data[0]
            student_name = student_data[1]
            program_code = student_data[2]
            courses = student_data[3:]

            print(f"Student ID: {student_id}")
            print(f"Student Name: {student_name}")
            print(f"Program Code: {program_code}")
            print("Courses:")

            for course in courses:
                course_code, course_score = course.split(":")
                print(f"- Course Code: {course_code}, Course Score: {course_score}")

            print()


def list_teachers():
    course_info = {}
    with open("course_info.txt", "r") as file:
        for line in file:
            course_data = line.strip().split(",")
            course_code = course_data[0]
            course_name = course_data[1]
            course_info[course_code] = course_name

    with open("teacher_info.txt", "r") as file:
        for line in file:
            teacher_data = line.strip().split(",")
            staff_id = teacher_data[0]
            teacher_name = teacher_data[1]
            courses = teacher_data[2:]

            print(f"Staff ID: {staff_id}")
            print(f"Teacher name: {teacher_name}")
            print("Teaches the following courses:")
            for course in courses:
                course_code = course.split(":")[0]
                course_name = course_info.get(course_code)
                print(f" - {course_code}: {course_name}")
            print()


def search_student():
    search_query = input("Enter student name or ID to search: ")

    with open("student_info.txt", "r") as file:
        found = False
        for line in file:
            student_data = line.strip().split(",")
            student_id = student_data[0]
            student_name = student_data[1]

            if search_query.lower() in student_id.lower() or search_query.lower() in student_name.lower():
                program_code = student_data[2]
                courses = student_data[3:]

                print(f"Student ID: {student_id}")
                print(f"Student Name: {student_name}")
                print(f"Program Code: {program_code}")
                print("Courses:")

                for course in courses:
                    course_code, course_score = course.split(":")
                    print(f"- Course Code: {course_code}, Course Score: {course_score}")

                print()

                found = True

        if not found:
            print("Student not found.")
            print()


def get_credit_hours(course_code):
    with open("course_info.txt", "r") as file:
        for line in file:
            course_data = line.strip().split(",")
            if course_data[0] == course_code:
                return int(course_data[2])

    return 0


def calculate_grade(score):
    grade_ranges = {
        (80, 101): 4.00,
        (75, 80): 3.67,
        (70, 75): 3.33,
        (65, 70): 3.00,
        (60, 65): 2.67,
        (55, 60): 2.33,
        (50, 55): 2.00,
        (47, 50): 1.67,
        (44, 47): 1.33,
        (40, 44): 1.00,
    }

    for range_start, range_end in grade_ranges:
        if range_start <= score < range_end:
            return grade_ranges[(range_start, range_end)]

    return 0.00


def student_gpa(courses, total_credit_hours=0, total_grade_points=0):
    # Base case: If no courses left, return calculated GPA
    if len(courses) == 0:
        if total_credit_hours == 0:
            return 0.0
        else:
            return total_grade_points / total_credit_hours

    # Recursive case: Calculate GPA recursively
    course, score = courses[0]
    credit_hours = get_credit_hours(course)
    grade = calculate_grade(score)

    return student_gpa(courses[1:],total_credit_hours + credit_hours,total_grade_points + (grade * credit_hours))


def list_teachers_courses():
    with open("teacher_info.txt", "r") as file:
        for line in file:
            teacher_data = line.strip().split(",")
            staff_id = teacher_data[0]
            teacher_name = teacher_data[1]
            courses = teacher_data[2].split(":")

            print(f"Staff ID: {staff_id}")
            print(f"Teacher Name: {teacher_name}")
            print("Teaches the following courses:")
            for course in courses:
                print(course)
            print()


def course_gpa():
    with open("course_info.txt", "r") as file:
        for line in file:
            course_data = line.strip().split(",")
            course_code = course_data[0]
            course_name = course_data[1]
            credit_hours = course_data[2]

            print(f"Course Code: {course_code}  Credit Hours: {credit_hours}")

            print()


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

        elif choice == "3":
            add_teacher()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_teachers()
        elif choice == "6":
            search_student()
        elif choice == "7":
            list_teachers_courses()
        elif choice == "8":
            course_gpa()
        else:
            print("Wrong menu selection.")
            print()

for file_name in ["student_info.txt", "course_info.txt", "teacher_info.txt"]:
    if not os.path.exists(file_name):
        open(file_name, "w").close()

#ls = [('CSC300',45), ('ITS230',90)]
#print(student_gpa(ls))
main()