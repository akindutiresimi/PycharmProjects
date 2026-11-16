from user import User


class Customer(User):
    def __init__(self, name: str, phone_number: str):
        super().__init__(name, phone_number)
        self._customer_id = None
        self._cart = {}

    @property
    def id(self):
        return self._customer_id

    @id.setter
    def id(self, value):
        self._customer_id = value

    @property
    def cart(self):
        return self._cart