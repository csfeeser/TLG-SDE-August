#!/usr/env/python3

main()

def main()
    students = [
        "Amir", "Breana", "Katie", "Clayton", "Coty", "Daiyron",
        "Douglas", "Gabriel", "Jakira", "John", "Jonathan",
        "Justin", "Megan", "Tayo", "Summer", "Tomiwa"

    # len() function counts up how many names in the list
    headcount = len(students)

    str_number = input(f"Pick a number between 1 and {headcount}: ")

    # int() function converts a string into an integer
    int_number = int(str_number)

    student_choice = students[str_number]

    print("{student_choice} is AWESOME!")