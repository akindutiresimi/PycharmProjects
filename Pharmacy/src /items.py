from datetime import date


class Item:
    def __init__(self, name: str, expiry_date: date, price: int, quantity: int = 1):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._name = name
        self._expiry_date = expiry_date
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date: date):
        self._expiry_date = expiry_date

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: int):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price

    @property
    def quantity(self) :
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = quantity