class Transaction:

    def __init__(self, fuel_name: str, liters: float, price_per_liter: float):
        self.fuel_name = fuel_name
        self.liters = liters
        self.price_per_liter = price_per_liter
        self.total = liters * price_per_liter

    def __str__(self):
        return (f"{self.fuel_name}: {self.liters:.2f}L "
                f"@ {self.price_per_liter} = {self.total:.2f}")


class TransactionHistory:
    def __init__(self):
        self._transactions = []

    def add(self, transaction: Transaction):
        self._transactions.append(transaction)

    def all(self) -> list:
        return list(self._transactions)

    def total_sales(self) -> float:
        return sum(t.total for t in self._transactions)