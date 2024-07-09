class BankAccount:
    def __init__(self, accountNumber, accountHolder, initialBalance):
        self.__accountNumber = accountNumber
        self.__accountHolder = accountHolder
        self.__balance = initialBalance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("You must enter a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("No funds available.")
        else:
            print("Withdrawal amount has to be a postive number.")

    def getBalance(self):
        return self.__balance

    def displayAccountInfo(self):
        print(f"Account Number: {self.__accountNumber}")
        print(f"Account Holder: {self.__accountHolder}")
        print(f"Balance: ${self.__balance:.2f}")


def main():
    # Instantiate bank account objects
    account1 = BankAccount("1", "Javier Ibanez", 1000)
    account2 = BankAccount("2", "Leonardo Ibanez", 500)

    # Perform transaction methods
    account1.deposit(100)
    account1.withdraw(20)
    account2.deposit(100)
    # Should display an error message
    account2.withdraw(500)

    # Display updated account information
    account1.displayAccountInfo()
    print()
    account2.displayAccountInfo()


if __name__ == "__main__":
    main()
