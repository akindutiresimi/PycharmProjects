from user import User


class Pharmacist(User):
    def __init__(self, name: str, phone_number: str, pharmacist_id: int):
        super().__init__(name, phone_number)
        self._pharmacist_id = pharmacist_id

    @property
    def id(self):
        return self._pharmacist_id

    @id.setter
    def id(self, value: int):
        self._pharmacist_id = value