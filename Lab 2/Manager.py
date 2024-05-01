from Employee import Employee
import mysql.connector


class Manager(Employee):
    def __init__(
        self, firstName, lastName, age, department, salary, managed_department
    ):
        super().__init__(firstName, lastName, age, department, salary)
        self.managed_department = managed_department

    @classmethod
    def show(cls, employee_id):
        conn = mysql.connector.connect(**cls.db_config)
        cursor = conn.cursor()

        sql = "SELECT * FROM employees WHERE id = %s"
        cursor.execute(sql, (employee_id,))
        employee = cursor.fetchone()

        if employee:
            print(f"First Name: {employee[1]}")
            print(f"Last Name: {employee[2]}")
            print(f"Age: {employee[3]}")
            print(f"Department: {employee[4]}")
            print("Salary: Confidential")
            if isinstance(cls, Manager):
                print(f"Managed Department: {employee[6]}")
        else:
            print("Employee not found with ID:", employee_id)

        cursor.close()
        conn.close()

    # overrides save method
    def save_to_database(self):
        conn = mysql.connector.connect(**self.db_config)
        cursor = conn.cursor()

        sql = "INSERT INTO employees (firstName, lastName, age, department, salary, managed_department) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (
            self.firstName,
            self.lastName,
            self.age,
            self.department,
            self.salary,
            self.managed_department,
        )

        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()


mgr = Manager("alex", "Doeeaas", 30, "IT", 5000.00, "IT")
mgr.save_to_database()  # Save the manager data to the database
