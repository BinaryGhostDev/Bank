import mysql.connector

def connect_to_database():
    try:
        # Adjust the connection parameters based on your MySQL configuration
        db = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="bank"
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_tables():
    db = connect_to_database()
    if not db:
        return

    try:
        cursor = db.cursor()

        # Create 'accounts' table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                dob DATE NOT NULL,
                aadhar_card_number VARCHAR(12) NOT NULL,
                account_number VARCHAR(12) NOT NULL,
                mobile_number VARCHAR(10) NOT NULL,
                address TEXT,
                branch_name VARCHAR(255) NOT NULL,
                branch_code VARCHAR(10) NOT NULL,
                ifsc_code VARCHAR(11) NOT NULL,
                password VARCHAR(255) NOT NULL,
                pin VARCHAR(4) NOT NULL,
                balance INT DEFAULT 0
            )
        """)

        # Create 'users' table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                role ENUM('employee', 'manager') NOT NULL,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL
            )
        """)

        # Create 'transactions' table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                account_number VARCHAR(12) NOT NULL,
                transaction_type VARCHAR(50),
                amount DECIMAL(10, 2) NOT NULL,
                transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Insert dummy data for an admin user
        cursor.execute("""
            INSERT INTO users (username, password, role, first_name, last_name)
            VALUES ('RajanGoswami', 'admin', 'manager', 'Rajan', 'Goswami')
        """)

        # Insert dummy data for an admin user
        cursor.execute("""
            INSERT INTO users (username, password, role, first_name, last_name)
            VALUES ('Admin', 'admin', 'manager', 'admin', 'admin')
        """)

        db.commit()
        print("Tables created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if db.is_connected():
            cursor.close()
            db.close()

# Call the function to create tables and insert dummy data
create_tables()
