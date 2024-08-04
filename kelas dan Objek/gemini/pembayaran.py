class Payment:
    def __init__(self, amount, method):
        self.amount = amount
        self.method = method

    def process(self):
        print(f"Processing payment of ${self.amount} via {self.method}")

payment1 = Payment(10000, "Credit Card")

payment1.process()

payment2 = Payment(50000, "Cash")

payment2.process()