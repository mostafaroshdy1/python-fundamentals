from Employee import Employee
from Manager import Manager


def main():
    while True:
        menu()
        choice = input("Enter your choice: ").lower()

        if choice == "e":
            add_employee()
        elif choice == "m":
            add_manager()
        elif choice == "s":
            Employee.print_all_employees()
        elif choice == "q":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


def add_employee():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    age = int(input("Enter the age: "))
    department = input("Enter the department: ")
    salary = float(input("Enter the salary: "))

    emp = Employee(first_name, last_name, age, department, salary)
    emp.save_to_database()
    print("Employee added successfully.")


def add_manager():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    age = int(input("Enter the age: "))
    department = input("Enter the department: ")
    salary = float(input("Enter the salary: "))
    managed_department = input("Enter the managed department: ")

    manager = Manager(
        first_name, last_name, age, department, salary, managed_department
    )
    manager.save_to_database()
    print("Manager added successfully.")


def menu():
    print("Menu:")
    print("1. Add new employee (press 'e')")
    print("2. Add new manager (press 'm')")
    print("3. Show all employees (press 's')")
    print("4. Quit (press 'q')")


if __name__ == "__main__":
    main()
