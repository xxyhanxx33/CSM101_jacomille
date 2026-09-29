
jacomille_records = {
    "Liza": {
        "StudID": "S001",
        "Grade": [90, 85, 86, 82, 89, 90, 92]
    },
    "Jeremy": {
        "StudID": "S002",
        "Grade": [72, 75, 69, 80, 54, 75, 85]
    }
}


jacomille_name = str(input("Enter the student name to search: ")).title()

if jacomille_name in jacomille_records:
    print(f"Student '{jacomille_name}' is found.")

    jacomille_student_data = jacomille_records[jacomille_name]
    jacomille_grades = jacomille_student_data["Grade"]


    print(f"Student ID: {jacomille_student_data['StudID']}")
    print(f"Grades: {jacomille_grades}")


    jacomille_average = sum(jacomille_grades) / len(jacomille_grades)
    print(f"Average Grade: {jacomille_average:.2f}")


    jacomille_has_low_grade = any(jacomille_grade < 60 for jacomille_grade in jacomille_grades)
    if jacomille_has_low_grade:
        print("Candidate for intervention")


    jacomille_highest = max(jacomille_grades)
    print(f"Highest Grade: {jacomille_highest}")

    jacomille_lowest = min(jacomille_grades)
    print(f"Lowest Grade: {jacomille_lowest}")

else:
    print(f"Student '{jacomille_name}' is not found.")