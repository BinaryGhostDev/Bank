from src.db_connector import connect_to_database
from src.text_color import success_message, error_message

def format_balance(balance):
    return '{:,.2f}'.format(balance)

def withdraw_balance_by_cheque():
    # Connect to the MySQL database
    db = connect_to_database()

    if not db:
        return

    try:
        cursor = db.cursor()

        # Ask for the account number on the cheque
        account_number_on_cheque = input("Enter the account number on the cheque: ")

        # Check if the account exists
        cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number_on_cheque,))
        account = cursor.fetchone()

        if not account:
            error_message("Account not found.")
            return

        # Ask for the cheque number
        cheque_number = input("Enter the cheque number: ")

        # Ask for the amount on the cheque
        cheque_amount = float(input("Enter the amount on the cheque: "))

        # Confirm debit operation
        confirm = input(f"Do you want to debit ₹{cheque_amount} from account {account_number_on_cheque}? (y/n): ").lower()

        if confirm != 'y':
            error_message("Withdrawal operation cancelled.")
            return

        # Check if the account has sufficient balance
        if account[14] < cheque_amount:
            error_message("Insufficient balance. Withdrawal operation cancelled.")
            return

        # Update the balance in the 'accounts' table
        updated_balance = account[14] - cheque_amount
        cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s", (updated_balance, account_number_on_cheque))

        # Store the transaction in the 'transactions' table
        cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, 'debit by Cheque', %s)",
                       (account_number_on_cheque, cheque_amount))

        db.commit()
        formatted_balance = format_balance(updated_balance)
        success_message(f"Withdrawal by cheque successful. Updated Balance: ₹ {formatted_balance}")

    except mysql.connector.Error as err:
        db.rollback()
        error_message(f"Error: {err}")

    finally:
        # Close the database connection
        if db.is_connected():
            cursor.close()
            db.close()
