from src.db_connector import connect_to_database
import mysql.connector
from prettytable import PrettyTable
from src.text_color import success_message, error_message

def show_employees():
    # Connect to the MySQL database
    db = connect_to_database()

    if not db:
        return

    try:
        cursor = db.cursor()

        print("1. Show all employees")
        print("2. Search by employee ID")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            # Show all employees
            cursor.execute("SELECT * FROM users")
            employees = cursor.fetchall()

            if employees:
                print("")
                success_message("All Employees:")
                display_table(employees)
            else:
                error_message("No employees found.")

        elif choice == '2':
            # Search by employee ID
            employee_id = input("Enter employee ID: ")
            cursor.execute("SELECT * FROM users WHERE id = %s", (employee_id,))
            employee = cursor.fetchone()

            if employee:
                success_message("Employee Found:")
                display_table([employee])
            else:
                error_message("Employee not found.")

        else:
            error_message("Invalid choice. Please enter 1 or 2.")

    except mysql.connector.Error as err:
        error_message(f"Error: {err}")

    finally:
        # Close the database connection
        if db.is_connected():
            cursor.close()
            db.close()

def display_table(data):
    # Create a PrettyTable
    table = PrettyTable()

    # Set the column names
    table.field_names = ["ID", "Username", "Password", "Role", "First Name", "Last Name"]

    # Add rows to the table
    for row in data:
        table.add_row(row)

    # Print the table
    print(table)
