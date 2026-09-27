class Account:
    def __init__(self, name: str) -> None:
        self.name = name.lower()
        self.balance = 0

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit cannot be negative")
        self.balance += amount


    def withdraw(self, amount: float):
        if (self.balance < amount and amount > 0):
            raise ValueError("Withdraw cannot be negative")
        self.balance -= amount

