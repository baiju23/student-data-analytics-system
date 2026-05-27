# Import CSV Module

import csv


# ==================================================
# FILE NAME
# ==================================================

FILE_NAME = "students.csv"


# ==================================================
# ADD STUDENT FUNCTION
# ==================================================

def add_student():

    print("\n===== Add Student =====")

    # Take Student Name
    name = input("Enter Student Name: ")

    try:
        # Take Student Marks
        marks = int(input("Enter Student Marks: "))

    except ValueError:

        print("Invalid Marks!")
        return

    # Open CSV File in Append Mode
    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        # Write Data Into CSV
        writer.writerow([name, marks])

    print("Student Added Successfully")


# ==================================================
# VIEW STUDENT FUNCTION
# ==================================================

def view_student():

    print("\n===== Student Records =====")

    try:
        # Open CSV File in Read Mode
        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)

            # Read Each Row
            for row in reader:

                print(f"Name: {row[0]} | Marks: {row[1]}")

    except FileNotFoundError:

        print("No Student Data Found")


# ==================================================
# SEARCH STUDENT FUNCTION
# ==================================================

def search_student():

    print("\n===== Search Student =====")

    search_name = input("Enter Student Name To Search: ")

    found = False

    try:
        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)

            # Search Student
            for row in reader:

                if row[0].strip().lower() == search_name.strip().lower():

                    print(f"Found -> Name: {row[0]} | Marks: {row[1]}")

                    found = True

            # If Student Not Found
            if not found:

                print("Student Not Found")

    except FileNotFoundError:

        print("No Student Data Available")


# ==================================================
# DELETE STUDENT FUNCTION
# ==================================================

def delete_student():

    print("\n===== Delete Student =====")

    delete_name = input("Enter Student Name To Delete: ")

    updated_students = []

    found = False

    try:
        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)

            # Check Each Student
            for row in reader:

                # Keep Other Students
                if row[0].strip().lower() != delete_name.strip().lower():

                    updated_students.append(row)

                else:

                    found = True

        # Rewrite CSV File
        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(updated_students)

        if found:

            print("Student Deleted Successfully")

        else:

            print("Student Not Found")

    except FileNotFoundError:

        print("No Student Data Available")


# ==================================================
# FIND TOPPER FUNCTION
# ==================================================

def topper_student():

    print("\n===== Find Topper =====")

    topper_name = ""

    highest_marks = -1

    try:
        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)

            # Find Highest Marks
            for row in reader:

                marks = int(row[1])

                if marks > highest_marks:

                    highest_marks = marks

                    topper_name = row[0]

        if highest_marks != -1:

            print(f"Topper: {topper_name} | Marks: {highest_marks}")

    except FileNotFoundError:

        print("No Student Data Found")


# ==================================================
# AVERAGE MARKS FUNCTION
# ==================================================

def average_marks():

    print("\n===== Average Marks =====")

    total_marks = 0

    total_students = 0

    try:
        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)

            # Calculate Total Marks
            for row in reader:

                total_marks += int(row[1])

                total_students += 1

        if total_students > 0:

            average = total_marks / total_students

            print(f"Average Marks: {average:.2f}")

        else:

            print("No Student Records Found")

    except FileNotFoundError:

        print("No Student Data Found")


# ==================================================
# MAIN MENU
# ==================================================

while True:

    print("\n===================================")
    print(" STUDENT DATA ANALYTICS SYSTEM ")
    print("===================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Find Topper")
    print("6. Average Marks")
    print("7. Exit")

    # Take User Choice
    choice = input("\nEnter Choice: ")

# ==================================================
# MENU CONDITIONS
# ==================================================

    if choice == "1":

        add_student()

    elif choice == "2":

        view_student()

    elif choice == "3":

        search_student()

    elif choice == "4":

        delete_student()

    elif choice == "5":

        topper_student()

    elif choice == "6":

        average_marks()

    elif choice == "7":

        print("\nProgram Closed Successfully")

        break

    else:

        print("\nInvalid Choice! Please Try Again.")