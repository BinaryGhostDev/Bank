from src.db_connector import connect_to_database
from src.text_color import success_message, error_message

def format_balance(balance):
    return '{:,.2f}'.format(balance)

def debit_balance():
    # Connect to the MySQL database
    db = connect_to_database()

    if not db:
        return

    try:
        cursor = db.cursor()

        # Ask for the account number
        account_number = input("Enter account number to debit: ")

        # Check if the account exists
        cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number,))
        account = cursor.fetchone()

        if not account:
            error_message("Account not found.")
            return

        # Display account information
        print("Account Information:")
        print(f"Full Name: {account[2]} {account[3]}")  # Assuming first_name is at index 2 and last_name is at index 3
        print(f"Date of Birth: {account[4]}")
        print(f"PIN: {account[13]}")

        # Confirm if it's the correct account
        confirm = input("Is this your correct account? (y/n): ").lower()

        if confirm != 'y':
            error_message("Debit operation cancelled.")
            return

        # Ask for the amount to debit
        amount = float(input("Enter the amount to debit: "))

        # Check if the account has sufficient balance
        if account[14] < amount:
            error_message("Insufficient balance. Debit operation cancelled.")
            return

        # Update the balance in the 'accounts' table
        updated_balance = account[14] - amount
        cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s", (updated_balance, account_number))

        # Store the transaction in the 'transactions' table
        cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, 'debit', %s)",
                       (account_number, amount))

        db.commit()
        formatted_balance = format_balance(updated_balance)
        success_message(f"Balance debited successfully. Updated Balance: ₹ {formatted_balance}")

    except mysql.connector.Error as err:
        db.rollback()
        error_message(f"Error: {err}")

    finally:
        # Close the database connection
        if db.is_connected():
            cursor.close()
            db.close()
