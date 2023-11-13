def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")
def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
def check_balance(self):
         print(f"Account balance for{self.account_holder}: ${self.balance}")
# Example usage:
# Create a bank account