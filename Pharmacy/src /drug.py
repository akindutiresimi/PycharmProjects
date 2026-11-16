from datetime import date
from item import Item


class Drug(Item):
    def __init__(self, name: str, expiry_date: date, price: int, quantity: int = 1):
        super().__init__(name, expiry_date, price, quantity)
