from user import User


class Admin(User):
    def __init__(self, name: str, phone_number: str, admin_id: int):
        super().__init__(name, phone_number)
        self._admin_id = admin_id

    @property
    def id(self) :
        return self._admin_id

    @id.setter
    def id(self, value: int):
        self._admin_id = value