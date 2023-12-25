from src.db_connector import connect_to_database
from src.text_color import success_message, error_message
import mysql.connector

def format_balance(balance):
    return '{:,.2f}'.format(balance)

def transfer_balance():
    # Connect to the MySQL database
    db = connect_to_database()

    if not db:
        return

    try:
        cursor = db.cursor()

        # Ask for the account number to transfer to
        recipient_account_number = input("Enter recipient's account number: ")

        # Check if the recipient account exists
        cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (recipient_account_number,))
        recipient_account = cursor.fetchone()

        if not recipient_account:
            error_message("Recipient account not found.")
            return

        # Ask for the sender's own account number
        sender_account_number = input("Enter sender account number: ")

        # Check if the sender's account exists
        cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (sender_account_number,))
        sender_account = cursor.fetchone()

        if not sender_account:
            error_message("Your account not found.")
            return

        # Check if the recipient account and sender account are the same
        if recipient_account_number == sender_account_number:
            error_message("Recipient account and Sender account cannot be the same.")
            return
        else:
            pass

        # Display sender and recipient information
        print("")
        error_message("Sender Information:")
        print(f"Full Name: {sender_account[2]} {sender_account[3]}")  # Assuming first_name is at index 2 and last_name is at index 3
        print("")
        success_message("Recipient Information:")
        print(f"Full Name: {recipient_account[2]} {recipient_account[3]}")

        # Confirm if it's the correct transfer
        print("")
        confirm = input("Is this the correct transfer? (y/n): ").lower()

        if confirm != 'y':
            error_message("Transfer operation cancelled.")
            return

        # Ask for the amount to transfer
        amount = float(input("Enter the amount to transfer: "))

        # Check if the sender's account has sufficient balance
        if sender_account[14] < amount:
            error_message("Insufficient balance. Transfer operation cancelled.")
            return

        # Confirm the transfer
        print("")
        confirm_transfer = input(f"Are you sure you want to transfer ₹{amount} to {recipient_account[2]}? (y/n): ").lower()

        if confirm_transfer != 'y':
            error_message("Transfer operation cancelled.")
            return

        # Update the balances in the 'accounts' table
        updated_sender_balance = sender_account[14] - amount
        updated_recipient_balance = recipient_account[14] + amount

        cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s", (updated_sender_balance, sender_account_number))
        cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s", (updated_recipient_balance, recipient_account_number))

        # Store the transaction in the 'transactions' table for both sender and recipient
        cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, 'debit', %s)",
                       (sender_account_number, amount))
        cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, 'credit', %s)",
                       (recipient_account_number, amount))

        db.commit()
        formatted_balance = format_balance(updated_sender_balance)
        success_message(f"Balance transferred successfully. Updated Sender Balance: ₹ {formatted_balance}")

    except mysql.connector.Error as err:
        db.rollback()
        error_message(f"Error: {err}")

    finally:
        # Close the database connection
        if db.is_connected():
            cursor.close()
            db.close()
