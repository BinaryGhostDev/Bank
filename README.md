# Bank Management System (SCHOOL PROJECT)

Bank Management System: A user-friendly Python project for education and personal finance. Seamlessly manage accounts, ensure security, and track transactions. Ideal for learning programming and practical personal finance management.

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](https://opensource.org/licenses/AGPL-3.0)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)

🏦 Welcome to the Bank project! This Python-based banking system allows users to create accounts, perform transactions, and manage finances securely.

[![Watch the Vimeo video](https://i.postimg.cc/NFqgKv6J/BANK-MANAGEMENT-RAJAN.png)](https://vimeo.com/897814966?share=copy)

## Features

- 🌐 Multi-user support with role-based access (e.g., admin, employee, customer).
- 💳 Create bank accounts with unique account numbers and secure PINs.
- 🔄 Perform transactions, view balances, and manage account details.
- 📊 Transaction history and account management functionalities.
- 🚀 Easy-to-use command-line interface.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation for Linux or Ubuntu

* If you are Windows users, you can zip download and follow the same process.

1. Clone the repository:

   ```bash
   git clone https://github.com/rajanGoswamiDev/Bank.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Bank
   ```

3. Install dependencies:

* Change these details from (requirements.txt) 'your_username'@'localhost' IDENTIFIED BY 'your_password' as per your MySql Credentials.

   ```bash
   pip install -r requirements.txt
   ```

Certainly! Here's a formatted version of the "Usage" section:

## Usage

### 1. Create and initialize database tables:

* Update these details from `db.py`: `user="your_username"`, `password="your_password"`, `database="your_database_name"`.

   - Insert dummy data for an admin user:
     ```sql
     INSERT INTO users (username, password, role, first_name, last_name) VALUES ('your_username', 'your_password', 'manager', 'your_first_name', 'your_last_name')
     ```
     
   ```bash
   python db.py
   ```


### 2. Run the application:

   ```bash
   python main.py
   ```

### 3. Follow the on-screen prompts to navigate through the banking system.

## Contributing

* Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

Donate ❤️ Upi Id - rajangoswami@fam

## License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.
