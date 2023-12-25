from src.db_connector import connect_to_database
import mysql.connector
from prettytable import PrettyTable
from src.text_color import success_message, error_message

def show_account_holders():
    # Connect to the MySQL database
    db = connect_to_database()

    if not db:
        return

    try:
        cursor = db.cursor()

        print("1. Show all account holders")
        print("2. Search by account holder ID")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            # Show all account holders
            cursor.execute("SELECT id, username, first_name, last_name, dob, aadhar_card_number, "
                           "account_number, mobile_number, address, branch_name, branch_code, ifsc_code, "
                           "password, pin, balance FROM accounts")
            account_holders = cursor.fetchall()

            if account_holders:
                success_message("All Account Holders:")
                display_table(account_holders)
            else:
                error_message("No account holders found.")

        elif choice == '2':
            # Search by account holder ID
            account_number = input("Enter account number: ")
            cursor.execute("SELECT id, username, first_name, last_name, dob, aadhar_card_number, "
                           "account_number, mobile_number, address, branch_name, branch_code, ifsc_code, "
                           "password, pin, balance FROM accounts WHERE account_number = %s", (account_number,))
            account_holder = cursor.fetchone()

            if account_holder:
                success_message("Account Holder Found:")
                display_table([account_holder])
            else:
                error_message("Account holder not found.")

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
    table.field_names = ["ID", "Username", "First Name", "Last Name", "DOB", "Aadhar Card Number",
                         "Account Number", "Mobile Number", "Address", "Branch Name", "Branch Code",
                         "IFSC Code", "Password", "PIN", "Balance"]

    # Add rows to the table
    for row in data:
        table.add_row(row)

    # Print the table
    print(table)