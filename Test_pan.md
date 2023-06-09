add_course

| Test ID | Test Category | Description                        | Input                                   | Expected Output                    | Status |
|---------|---------------|------------------------------------|-----------------------------------------|------------------------------------|--------|
| TC1     | Positive      | Adding a course successfully        | Course code: "CSE101", Credit hour: "3" | Course added successfully          |        |
| TC2     | Positive      | Adding a course successfully        | Course code: "MAT201", Credit hour: "4" | Course added successfully          |        |
| TC3     | Negative      | Adding a course with invalid inputs  | Course code: "", Credit hour: "2"       | Invalid course code                 |        |
| TC4     | Negative      | Adding a course with invalid inputs  | Course code: "PHY301", Credit hour: ""  | Invalid credit hour                 |        |
| TC5     | Edge          | Adding a course with maximum inputs  | Course code: "BIO101", Credit hour: "5" | Course added successfully          |        |
| TC6     | Edge          | Adding a course with minimum inputs  | Course code: "ENG201", Credit hour: "1" | Course added successfully          |        |

add_student

| Test ID | Test Category | Description                        | Input                                                        | Expected Output                    | Status |
|---------|---------------|------------------------------------|--------------------------------------------------------------|------------------------------------|--------|
| TC1  | Positive      | Adding a student successfully       | Student ID: "1234", Name: "John Doe", Course codes: ["CSE101"] | Student added successfully         |        |
| TC2  | Positive      | Adding a student successfully       | Student ID: "5678", Name: "Jane Smith", Course codes: ["MAT201", "PHY301"] | Student added successfully         |        |
| TC3  | Negative      | Adding a student with invalid inputs | Student ID: "", Name: "John Doe", Course codes: ["CSE101"]     | Invalid student ID                 |        |
| TC4  | Negative      | Adding a student with invalid inputs | Student ID: "1234", Name: "", Course codes: ["CSE101"]         | Invalid student name               |        |
| TC5  | Edge          | Adding a student with maximum inputs | Student ID: "9999", Name: "John Doe", Course codes: ["CSE101", "MAT201", "PHY301"] | Student added successfully         |        |
| TC6  | Edge          | Adding a student with minimum inputs | Student ID: "1111", Name: "John Doe", Course codes: []          | Student added successfully         |        |

... (similar tables for other functions)

is_valid_credit_hour

| Test ID | Test Category | Description                        | Input    | Expected Output | Status |
|---------|---------------|------------------------------------|----------|-----------------|--------|
| TC1     | Positive      | Valid credit hour within range      | "3"      | True            |        |
| TC2     | Positive      | Valid credit hour within range      | "5"      | True            |        |
| TC3     | Negative      | Invalid credit hour - less than 1   | "0"      | False           |        |
| TC4     | Negative      | Invalid credit hour - greater than 5| "6"      | False           |        |
| TC5     | Edge          | Minimum valid credit hour           | "1"      | True            |        |
| TC6     | Edge          | Maximum valid credit hour           | "5"      | True            |        |

