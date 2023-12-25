import random
import getpass
from src.db_connector import connect_to_database
from src.text_color import success_message, error_message

def create_bank_account():
    # Collect user input for creating a bank account
    username = input("Enter username: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    aadhar_card_number = input("Enter Aadhar card number (12 digits): ")
    mobile_number = input("Enter mobile number (10 digits): ")
    address = input("Enter address: ")
    
    # Set default values for branch-related information
    branch_name = "GlobalGuard Bank"
    branch_code = "00082"
    ifsc_code = "RJ00082"

    # Generate random values for account_number and pin
    account_number = str(random.randint(10**11, 10**12 - 1))
    pin = str(random.randint(1000, 9999))

    # Connect to the MySQL database
    db = connect_to_database()

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Insert the user data into the 'accounts' table
    insert_query = """
    INSERT INTO accounts 
    (username, first_name, last_name, dob, aadhar_card_number, 
    mobile_number, address, branch_name, branch_code, ifsc_code, 
    account_number, password, pin)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    insert_values = (
        username, first_name, last_name, dob, aadhar_card_number,
        mobile_number, address, branch_name, branch_code,
        ifsc_code,  # Set default IFSC code
        account_number, getpass.getpass("Enter password: "), pin  # Fix here
    )

    try:
        cursor.execute(insert_query, insert_values)
        db.commit()
        success_message(f"Bank account created successfully. Account Number: {account_number} & Pin: {pin}")
    except Exception as e:
        db.rollback()
        error_message(f"Error creating bank account: {e}")
    finally:
        # Close the database connection
        db.close()
