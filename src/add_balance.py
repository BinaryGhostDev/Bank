from src.db_connector import connect_to_database
import mysql.connector
from src.text_color import success_message, error_message

MAX_PIN_TRIALS = 3  # Maximum number of unsuccessful PIN trials before account block

def format_balance(balance):
    return '{:,.2f}'.format(balance)

def add_balance():
    db = connect_to_database()

    if not db:
        return

    try:
        cursor = db.cursor()

        # Ask for the account number
        account_number = input("Enter account number to add balance: ")

        # Check if the account exists
        cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number,))
        account = cursor.fetchone()

        if not account:
            print("Account not found.")
            return

        # Ask for PIN for verification
        pin_trials = 0
        while pin_trials < MAX_PIN_TRIALS:
            entered_pin = input("Enter your PIN: ")

            if entered_pin == account[13]:  # Assuming PIN is at index 13
                break
            else:
                pin_trials += 1
                error_message("Incorrect PIN. Please try again.")
        
        if pin_trials == MAX_PIN_TRIALS:
            error_message("Too many unsuccessful PIN attempts. Your account will be blocked for 24 hours.")

            return

        # Ask for the amount to add
        amount_to_add = float(input("Enter the amount to add: "))

        # Update the balance in the 'accounts' table
        updated_balance = account[14] + amount_to_add
        cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s", (updated_balance, account_number))

        # Store the transaction in the 'transactions' table
        cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, 'credit by employee', %s)",
                       (account_number, amount_to_add))

        db.commit()
        formatted_balance = format_balance(updated_balance)
        success_message(f"Balance added successfully. Updated Balance: ₹ {formatted_balance}")

    except mysql.connector.Error as err:
        db.rollback()
        error_message(f"Error: {err}")

    finally:
        if db.is_connected():
            cursor.close()
            db.close()
