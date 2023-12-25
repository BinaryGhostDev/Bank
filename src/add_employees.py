import getpass 
from src.db_connector import connect_to_database
from src.text_color import success_message, error_message

def add_employees():
    # Collect user input for adding an employee
    username = input("Enter employee username: ")
    password = getpass("Enter employee password: ")
    first_name = input("Enter employee first name: ")
    last_name = input("Enter employee last name: ")

    # Set a default role (e.g., 'employee')
    role = 'employee'

    # Connect to the MySQL database
    db = connect_to_database()

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Insert the employee data into the 'employees' table
    insert_query = """
    INSERT INTO users 
    (username, password, first_name, last_name, role)
    VALUES (%s, %s, %s, %s, %s)
    """
    insert_values = (username, password, first_name, last_name, role)

    try:
        cursor.execute(insert_query, insert_values)
        db.commit()
        success_message(f"Employee added successfully.")
    except Exception as e:
        db.rollback()
        error_message(f"Error adding employee: {e}")
    finally:
        # Close the database connection
        db.close()
