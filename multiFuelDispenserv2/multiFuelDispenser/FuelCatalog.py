from fuel import Fuel


class FuelCatalog:
    def __init__(self):
        self._fuels = {}

    def add(self, fuel: Fuel):
        self._fuels[fuel.name] = fuel

    def get(self, name: str) -> Fuel:
        name = name.lower()
        if name not in self._fuels:
            raise ValueError("Fuel type invalid, enter a valid type of fuel")
        return self._fuels[name]

    def names(self) -> list:
        return list(self._fuels)

    @classmethod
    def default(cls):
        catalog = cls()
        for name, price in [("petrol", 650), ("diesel", 720),
                            ("kerosene", 550), ("gas", 480)]:
            catalog.add(Fuel(name, price))
        return catalog