from src.db_connector import connect_to_database
from src.text_color import success_message, error_message
import mysql.connector

def format_balance(balance):
    return '{:,.2f}'.format(balance)

def check_balance():
    # Connect to the MySQL database
    db = connect_to_database()

    if not db:
        return

    try:
        cursor = db.cursor()

        # Ask for the account number
        account_number = input("Enter account number: ")

        # Check if the account exists
        query = "SELECT balance FROM accounts WHERE account_number = %s"
        cursor.execute(query, (account_number,))
        result = cursor.fetchone()

        if not result:
            error_message("Account not found.")
            return

        # Display the balance
        balance = result[0]
        formatted_balance = format_balance(balance)
        success_message(f"Account balance : ₹ {formatted_balance}")

    except mysql.connector.Error as err:
        error_message(f"Error: {err}")

    finally:
        # Close the database connection
        if db.is_connected():
            cursor.close()
            db.close()
