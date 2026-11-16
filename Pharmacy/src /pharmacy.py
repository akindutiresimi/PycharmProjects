
class Pharmacy:

    def __init__(self, pharmacist: "pharmacist", admin: "admin"):
        self._drugs: list["Drug"] = []
        self._items: list["Item"] = []
        self._admin = admin
        self._pharmacist = pharmacist


    @property
    def admin(self) -> "Admin":
        return self._admin

    @admin.setter
    def admin(self, admin: "Admin"):
        self._admin = admin


    @property
    def pharmacist(self) -> "Pharmacist":
        return self._pharmacist

    @pharmacist.setter
    def pharmacist(self, pharmacist: "Pharmacist"):
        self._pharmacist = pharmacist