class BankAccount:
    # Initialize the account with an optional starting balance (default = 0)
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    # Deposit money into the account
    def deposit(self, amount):
        self.account_balance += amount

    # Withdraw money if sufficient balance is available
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    # Display the current account balance
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
