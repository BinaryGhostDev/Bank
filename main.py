from getpass import getpass
from src.db_connector import connect_to_database
from src.create_bank_account import create_bank_account
from src.add_employees import add_employees
from src.show_employees import show_employees
from src.show_account_holders import show_account_holders
from src.credit_balance import credit_balance
from src.debit_balance import debit_balance
from src.transfer_balance import transfer_balance
from src.withdraw_balance_by_cheque import withdraw_balance_by_cheque
from src.add_balance import add_balance
from src.withdraw_balance import debit_balance
from src.update_users_details import update_users_details
from src.text_color import error_message
from src.preloader import letter_animation, progress_bar
from src.check_balance import check_balance

def create_banner(text, color='\033[1;33m'):
    banner_text = f'{color}{text}\033[0m'
    print(banner_text)

def login():
    try:
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")

        # Connect to the MySQL database
        db = connect_to_database()

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Query to check the user's role
        role_query = "SELECT role FROM users WHERE username = %s AND password = %s"
        role_values = (username, password)
        cursor.execute(role_query, role_values)
        user_role = cursor.fetchone()

        if user_role:
            role = user_role[0]

            if role in ['employee', 'manager']:
                # User is an employee or manager, show respective menu
                if role == 'manager':
                    manager_menu()
                else:
                    employee_menu()
            else:
                error_message("Invalid role. Please try again.")
        else:
            error_message("Invalid username or password. Please try again.")

        # Close the database connection
        db.close()

    except KeyboardInterrupt:
        print("\nGood Bye ...")
        exit(1)

def show_menu(role):
    if role == 'manager':
        print("")
        print("1.  Create Bank Account")
        print("2.  Add Employees")
        print("3.  Show Employees")
        print("4.  Show Account Holders")
        print("5.  Credit Balance")
        print("6.  Debit Balance")
        print("7.  Transfer Balance")
        print("8.  Withdraw Balance By Cheque")
        print("9.  Check Balance")
        print("10. Update Users Details")
        print("11. Logged Out")
    elif role == 'employee':
        print("")
        print("1. Add Balance")
        print("2. Transfer Balance")
        print("3. Withdraw Balance")
        print("4. Withdraw Balance By Cheque")
        print("5. Check_Balance")
        print("6. Update Users Details")
        print("7. Logged Out")
    else:
        print("")
        error_message("Invalid choice.")

def manager_menu():
    while True:
        show_menu('manager')
        print("")
        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            create_bank_account()
        elif choice == '2':
            add_employees()
        elif choice == '3':
            show_employees()
        elif choice == '4':
            show_account_holders()
        elif choice == '5':
            credit_balance()
        elif choice == '6':
            debit_balance()
        elif choice == '7':
            transfer_balance()
        elif choice == '8':
            withdraw_balance_by_cheque()
        elif choice == '9':
            check_balance()
        elif choice == '10':
            update_users_details()
        elif choice == '11':
            print("Logged Out.")
            break
        else:
            error_message("Invalid choice. Please try again.")

def employee_menu():
    while True:
        show_menu('employee')
        print("")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_balance()
        elif choice == '2':
            transfer_balance()
        elif choice == '3':
            debit_balance()
        elif choice == '4':
            withdraw_balance_by_cheque()
        elif choice == '5':
            check_balance()
        elif choice == '6':
            update_users_details()
        elif choice == '7':
            print("Logged Out.")
            break
        else:
            error_message("Invalid choice. Please try again.")

# Show the progress bar for 5 seconds
# progress_bar(duration=5)
print("")
letter_animation()
progress_bar(duration=5)
print("")
create_banner(r"""
  ____ _       _           _  ____                     _   ____              _      _ 
 / ___| | ___ | |__   __ _| |/ ___|_   _  __ _ _ __ __| | | __ )  __ _ _ __ | | __ | |
| |  _| |/ _ \| '_ \ / _` | | |  _| | | |/ _` | '__/ _` | |  _ \ / _` | '_ \| |/ / | |
| |_| | | (_) | |_) | (_| | | |_| | |_| | (_| | | | (_| | | |_) | (_| | | | |   <  |_|
 \____|_|\___/|_.__/ \__,_|_|\____|\__,_|\__,_|_|  \__,_| |____/ \__,_|_| |_|_|\_\ (_)
""")


# Call the login function
login()
