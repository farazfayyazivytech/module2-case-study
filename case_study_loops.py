# Faraz Fayyaz
# case_study_loops
# This app will accept a student's name and GPA.
# This app will then test if student qualifies for Dean's List or Honor roll.

# student_name = accepts student name from user, removes padding
# full_name = splits full name into array of strings
# while loop executes if last name is not 'ZZZ'

student_name = input("Enter student's name: ").strip()
full_name = student_name.split()

while full_name[-1] != 'ZZZ':
    student_gpa = float(input("Enter studnet GPA: "))

    if student_gpa >= 3.5:
        print(student_name + " made the Dean's List!")
    elif student_gpa >= 3.25:
        print(student_name + " made Honor Roll!")
    break