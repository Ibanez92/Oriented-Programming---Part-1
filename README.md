# BankAccount Class Documentation

### Description
The `BankAccount` class is designed to manage bank accounts, allowing users to perform transactions and view account details.

### Attributes
- `__accountNumber (str)`: Unique identifier for the bank account.
- `__accountHolder (str)`: Name of the account holder.
- `__balance (int)`: Current balance of the account.

### Methods
- `__init__(self, accountNumber, accountHolder, initialBalance)`: Constructor to initialize the bank account with the provided account number, account holder name, and initial balance.
- `deposit(self, amount)`: Method to deposit a specified amount into the account and update the balance accordingly. Ensures the deposit amount is positive.
- `withdraw(self, amount)`: Method to withdraw a specified amount from the account and update the balance accordingly. Checks for sufficient balance and ensures the withdrawal amount is positive.
- `getBalance(self)`: Method to retrieve and return the current balance of the account.
- `displayAccountInfo(self)`: Method to display the account number, account holder name, and current balance.

## Running the Main Program

To run the main program, execute the `bankaccount.py` file. The program demonstrates the creation of multiple bank account objects, performs deposit and withdrawal transactions, and displays the account information for each account.
