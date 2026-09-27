from hmac import new


class MultiFuelDispenser:

    def __init__(self, liter: float= None, fuel_type: str = None, fuel_price: float = None):
        self.fuel_liter = liter
        self.fuel_type = fuel_type
        self.fuel_price = fuel_price

    def get_fuel_price(self):

        self.fuel_type = self.fuel_type.lower()

        if self.fuel_type == 'petrol':
            return 650
        elif self.fuel_type == 'diesel':
            return 720
        elif self.fuel_type == 'kerosene':
            return 550
        elif self.fuel_type == 'Gas':
           return 480
        else:
             raise ValueError(f'Fuel type invalid, enter a valid type of fuel')

    def get_fuel_liter(self):
        self.fuel_liter = self.fuel_type.lower()

        if self.fuel_type == 'petrol':
            return 1
        elif self.fuel_type == 'diesel':
            return 1
        elif self.fuel_type == 'kerosene':
            return 1
        elif self.fuel_type == 'Gas':
            return 1
        else:
            raise ValueError(f'Fuel type invalid, enter a valid type of fuel')

    def price(self, price: float):
        if self.fuel_liter is None:
            self.fuel_liter = price / self.fuel_price
        return self.fuel_liter

    def liter(self, liter: float):
        if liter < 0:
            raise ValueError(f'Fuel liter cannot be negative')

        else:
            self.fuel_liter = liter
            total_price = liter * self.fuel_price
            return total_price

    def cost(self, liter: float, price: float):
        if liter < 0 or price < 0:
            raise ValueError(f'Fuel price and liter cannot be negative')

        else:
            total_cost = liter * price
            return total_cost