class BankAccount:
    def __init__(self, name, account_number, balance, min_balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit {amount: .2f}. New balance: {self.balance: .2f}")

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            print(f"withdraw {amount: .2f}. New balance: {self.balance: .2f}")
        else:
            print(f"Insufficient funds. Minimum balance required: {self.min_balance:.2f}")

    def check_balance(self):
        print(f"Account balance: {self.balance: .2f}")


account1 = BankAccount('Farhan', 987868769866, 1000000, 700909)
account1.deposit(60000)
account1.withdraw(50000)
account1.check_balance()
