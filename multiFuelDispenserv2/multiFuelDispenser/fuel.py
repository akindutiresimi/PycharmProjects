class Fuel:
    def __init__(self, name: str, price_per_liter: float):
        if price_per_liter < 0:
            raise ValueError("Fuel price cannot be negative")
        self._name = name.lower()
        self._price_per_liter = price_per_liter

    @property
    def name(self) -> str:
        return self._name

    @property
    def price_per_liter(self) -> float:
        return self._price_per_liter

    def cost_for(self, liters: float) -> float:
        if liters < 0:
            raise ValueError("Fuel liter cannot be negative")
        return liters * self._price_per_liter

    def liters_for(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return amount / self._price_per_liter