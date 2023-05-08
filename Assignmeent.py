class SavingsAccount:
    def _init_(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful.")
        else:
            print("Insufficient funds for withdrawal.")

    def check_balance(self):
        print(f"Account balance: ${self.balance}")


# Example usage:
account = SavingsAccount (100) # Creating an account with an initial balance of $100
account.check_balance()  # Output: Account balance: $100

account.deposit(50)  # Deposit $50
account.check_balance()  # Output: Account balance: $150

account.withdraw(75)  # Withdraw $75
account.check_balance()  # Output: Account balance: $75

account.withdraw(100)  # Trying to withdraw $100 (insufficient funds)
account.check_balance()  # Output: Insufficient funds for withdrawal.