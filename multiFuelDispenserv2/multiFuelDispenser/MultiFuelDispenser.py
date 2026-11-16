from fuel_catalog import FuelCatalog
from transaction import Transaction, TransactionHistory


class MultiFuelDispenser:
    def __init__(self, fuel_type: str = None, liters: float = 0,
                 catalog: FuelCatalog = None, history: TransactionHistory = None):
        self._catalog = catalog or FuelCatalog.default()
        self._history = history or TransactionHistory()
        self._fuel = None
        self._liters = 0

        if fuel_type is not None:
            self.fuel_type = fuel_type
        self.liters = liters

    @property
    def fuel_type(self) -> str:
        return self._fuel.name if self._fuel else None

    @fuel_type.setter
    def fuel_type(self, value: str):
        self._fuel = self._catalog.get(value)

    @property
    def fuel_price(self) -> float:
        return self._fuel.price_per_liter if self._fuel else None

    @property
    def liters(self) -> float:
        return self._liters

    @liters.setter
    def liters(self, value: float):
        if value < 0:
            raise ValueError("Fuel liter cannot be negative")
        self._liters = value

    @property
    def history(self) -> TransactionHistory:
        return self._history

    def _require_fuel(self):
        if self._fuel is None:
            raise ValueError("Select a fuel type first")

    def liters_for_amount(self, amount: float) -> float:
        self._require_fuel()
        self._liters = self._fuel.liters_for(amount)
        return self._liters

    def total_price(self, liters: float = None) -> float:
        self._require_fuel()
        if liters is not None:
            self.liters = liters
        return self._fuel.cost_for(self._liters)

    def cost(self, liters: float, price: float) -> float:
        if liters < 0 or price < 0:
            raise ValueError("Fuel price and liter cannot be negative")
        return liters * price

    def dispense(self) -> Transaction:
        self._require_fuel()
        sale = Transaction(self._fuel.name, self._liters, self._fuel.price_per_liter)
        self._history.add(sale)
        return sale