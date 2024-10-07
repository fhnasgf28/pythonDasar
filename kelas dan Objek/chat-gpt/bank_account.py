class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('Invalid deposit Amount')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print('Invalid or isufficient funds for withdrawal')
    
    def get_balance(self):
        return self.balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print('Current balance', account.get_balance())