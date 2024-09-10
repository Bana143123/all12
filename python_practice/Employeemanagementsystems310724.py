import sqlite3
from prettytable import PrettyTable

# Database connection and setup
def connect():
    conn = sqlite3.connect('employee_management.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        position TEXT NOT NULL,
                        salary REAL NOT NULL)''')
    conn.commit()
    return conn

# Add Employee
def add_employee(name, age, position, salary):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, age, position, salary) VALUES (?, ?, ?, ?)", (name, age, position, salary))
    conn.commit()
    conn.close()
    print(f"Employee {name} added successfully.")

# Remove Employee
def remove_employee(employee_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id))
    conn.commit()
    conn.close()
    print(f"Employee with ID {employee_id} removed successfully.")

# Promote Employee
def promote_employee(employee_id, new_position, new_salary):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET position = ?, salary = ? WHERE id = ?", (new_position, new_salary, employee_id))
    conn.commit()
    conn.close()
    print(f"Employee with ID {employee_id} promoted to {new_position} with salary {new_salary}.")

# Display Employees
def display_employees():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()

    table = PrettyTable()
    table.field_names = ["ID", "Name", "Age", "Position", "Salary"]
    for row in rows:
        table.add_row(row)
    print(table)

# Main menu
def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Promote Employee")
        print("4. Display Employees")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            position = input("Enter position: ")
            salary = float(input("Enter salary: "))
            add_employee(name, age, position, salary)
        elif choice == "2":
            employee_id = int(input("Enter employee ID to remove: "))
            remove_employee(employee_id)
        elif choice == "3":
            employee_id = int(input("Enter employee ID to promote: "))
            new_position = input("Enter new position: ")
            new_salary = float(input("Enter new salary: "))
            promote_employee(employee_id, new_position, new_salary)
        elif choice == "4":
            display_employees()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
