from src.db_connector import connect_to_database
import mysql.connector
from src.text_color import success_message, error_message

def update_users_details():
    # Connect to the MySQL database
    db = connect_to_database()

    if not db:
        return

    try:
        cursor = db.cursor()

        # Ask for the account number
        account_number = input("Enter your account number: ")

        # Check if the account exists
        cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number,))
        account = cursor.fetchone()

        if not account:
            error_message("Account not found.")
            return

        # Display current user details
        print("Current User Details:")
        print(f"1. Name: {account[2]} {account[3]}")  # Assuming first_name is at index 2 and last_name is at index 3
        print(f"2. Mobile Number: {account[6]}")
        print(f"3. Aadhar Number: {account[7]}")
        print(f"4. Password: {account[12]}")
        print(f"5. PIN: {account[13]}")

        # Ask for updates
        update_name = input("Do you want to change your name? (y/n): ").lower()
        if update_name == 'y':
            new_first_name = input("Enter new first name: ")
            new_last_name = input("Enter new last name: ")
            cursor.execute("UPDATE accounts SET first_name = %s, last_name = %s WHERE account_number = %s",
                           (new_first_name, new_last_name, account_number))

        update_mobile = input("Do you want to change your mobile number? (y/n): ").lower()
        if update_mobile == 'y':
            new_mobile = input("Enter new mobile number: ")
            cursor.execute("UPDATE accounts SET mobile_number = %s WHERE account_number = %s",
                           (new_mobile, account_number))

        update_aadhar = input("Do you want to change your Aadhar number? (y/n): ").lower()
        if update_aadhar == 'y':
            new_aadhar = input("Enter new Aadhar number: ")
            cursor.execute("UPDATE accounts SET aadhar_number = %s WHERE account_number = %s",
                           (new_aadhar, account_number))

        update_password = input("Do you want to change your password? (y/n): ").lower()
        if update_password == 'y':
            new_password = input("Enter new password: ")
            cursor.execute("UPDATE accounts SET password = %s WHERE account_number = %s",
                           (new_password, account_number))

        update_pin = input("Do you want to change your PIN? (y/n): ").lower()
        if update_pin == 'y':
            new_pin = input("Enter new PIN: ")
            cursor.execute("UPDATE accounts SET pin = %s WHERE account_number = %s",
                           (new_pin, account_number))

        db.commit()
        success_message("User details updated successfully.")

    except mysql.connector.Error as err:
        db.rollback()
        error_message(f"Error: {err}")

    finally:
        # Close the database connection
        if db.is_connected():
            cursor.close()
            db.close()
