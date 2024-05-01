import mysql.connector


class Employee:
    db_config = {
        "host": "localhost",
        "port": "3306",
        "user": "root",
        "password": "root",
        "database": "python_labs",
    }

    def __init__(self, firstName, lastName, age, department, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.salary = salary
        self.department = department
        self.create_database()
        self.create_table()  # Create the employees table if it doesn't exist
        self.id = self.get_max_id() + 1

    def save_to_database(self):
        conn = mysql.connector.connect(**Employee.db_config)
        cursor = conn.cursor()

        sql = "INSERT INTO employees (id, firstName, lastName, age, department, salary) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (
            self.id,
            self.firstName,
            self.lastName,
            self.age,
            self.department,
            self.salary,
        )
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

    def create_database(self):
        conn = mysql.connector.connect(
            host=self.db_config["host"],
            port=self.db_config["port"],
            user=self.db_config["user"],
            password=self.db_config["password"],
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS python_labs")
        conn.commit()
        cursor.close()
        conn.close()

    def create_table(self):
        conn = mysql.connector.connect(
            host=self.db_config["host"],
            port=self.db_config["port"],
            user=self.db_config["user"],
            password=self.db_config["password"],
            database=self.db_config["database"],
        )
        cursor = conn.cursor()

        create_table_sql = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            firstName VARCHAR(255),
            lastName VARCHAR(255),
            age INT,
            department VARCHAR(255),
            managed_department VARCHAR(255),
            salary DECIMAL(10, 2)
        )
        """
        cursor.execute(create_table_sql)
        conn.commit()
        cursor.close()
        conn.close()

    def get_max_id(self):
        conn = mysql.connector.connect(**Employee.db_config)
        cursor = conn.cursor()

        sql = "SELECT MAX(id) FROM employees"
        cursor.execute(sql)
        max_id = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return max_id if max_id else 0

    def transfer(self, department):
        self.department = department

        conn = mysql.connector.connect(**Employee.db_config)
        cursor = conn.cursor()

        sql = "UPDATE employees SET department = %s WHERE id = %s"
        values = (self.department, self.id)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

    def fire(self):
        conn = mysql.connector.connect(**Employee.db_config)
        cursor = conn.cursor()

        sql = "DELETE FROM employees WHERE id = %s"
        values = (self.id,)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def show(cls, employee_id):
        conn = mysql.connector.connect(**cls.db_config)
        cursor = conn.cursor()

        sql = "SELECT * FROM employees WHERE id = %s"
        cursor.execute(sql, (employee_id,))
        employee = cursor.fetchone()

        if employee:
            print(employee)
        else:
            print("Employee not found with ID:", employee_id)

        cursor.close()
        conn.close()

    @classmethod
    def print_all_employees(cls):
        conn = mysql.connector.connect(**cls.db_config)
        cursor = conn.cursor()

        sql = "SELECT * FROM employees"
        cursor.execute(sql)
        employees = cursor.fetchall()

        for employee in employees:
            print(employee)

        cursor.close()
        conn.close()


emp = Employee("John", "Doeeaas", 30, "IT", 5000.00)
emp.save_to_database()  # Save the employee data to the database
