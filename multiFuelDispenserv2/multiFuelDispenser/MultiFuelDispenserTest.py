import unittest

# from multiFuelDispenser.MultiFuelDispenser import MultiFuelDispenser

from multiFuelDispenser.MultiFuelDispenser import MultiFuelDispenser
class MultiFuelDispenserTest(unittest.TestCase):

    def test_that_the_dispenser_has_the_selected_fuel_price(self):
        dispenser = MultiFuelDispenser(fuel_type='petrol')
        self.assertEqual(dispenser.fuel_price, 650)

    def test_invalid_fuel_type_raises_value_error(self):
        with self.assertRaises(ValueError):
            MultiFuelDispenser(fuel_type='rocket fuel')

    def test_that_changing_the_fuel_type_updates_the_price(self):
        dispenser = MultiFuelDispenser(fuel_type='petrol')
        dispenser.fuel_type = 'diesel'
        self.assertEqual(dispenser.fuel_price, 720)

    def test_that_setting_an_invalid_fuel_type_later_raises_value_error(self):
        dispenser = MultiFuelDispenser(fuel_type='petrol')
        with self.assertRaises(ValueError):
            dispenser.fuel_type = 'water'

    def test_that_the_price_cannot_be_set_directly(self):
        dispenser = MultiFuelDispenser(fuel_type='petrol')
        with self.assertRaises(AttributeError):
            dispenser.fuel_price = 1

    def test_that_the_amount_of_money_can_be_used_to_get_liters(self):
        dispenser = MultiFuelDispenser(fuel_type='petrol')
        result = dispenser.liters_for_amount(3000)
        self.assertEqual(round(result, 2), 4.62)

    def test_that_liters_for_amount_raises_error_if_no_fuel_is_selected(self):
        dispenser = MultiFuelDispenser()
        with self.assertRaises(ValueError):
            dispenser.liters_for_amount(3000)

    def test_that_a_negative_amount_raises_value_error(self):
        dispenser = MultiFuelDispenser(fuel_type='petrol')
        with self.assertRaises(ValueError):
            dispenser.liters_for_amount(-100)

    def test_that_when_liters_are_specified_the_total_price_is_shown(self):
        dispenser = MultiFuelDispenser(fuel_type='petrol')
        self.assertEqual(dispenser.total_price(4), 2600)

    def test_that_total_price_uses_the_liters_given_at_creation(self):
        dispenser = MultiFuelDispenser(fuel_type='diesel', liters=10)
        self.assertEqual(dispenser.total_price(), 7200)

    def test_that_total_price_raises_error_if_no_fuel_is_selected(self):
        dispenser = MultiFuelDispenser()
        with self.assertRaises(ValueError):
            dispenser.total_price(4)

    def test_that_negative_liters_raise_value_error(self):
        dispenser = MultiFuelDispenser(fuel_type='petrol')
        with self.assertRaises(ValueError):
            dispenser.total_price(-4)

    def test_that_liters_start_at_zero_by_default(self):
        dispenser = MultiFuelDispenser(fuel_type='petrol')
        self.assertEqual(dispenser.liters, 0)

    def test_that_setting_negative_liters_directly_raises_value_error(self):
        dispenser = MultiFuelDispenser(fuel_type='petrol')
        with self.assertRaises(ValueError):
            dispenser.liters = -1

    def test_that_when_a_client_buys_petrol_the_total_bill_is_shown(self):
        dispenser = MultiFuelDispenser()
        self.assertEqual(dispenser.cost(liters=4, price=650), 2600)

    def test_that_a_negative_liter_in_cost_raises_value_error(self):
        dispenser = MultiFuelDispenser()
        with self.assertRaises(ValueError):
            dispenser.cost(liters=-4, price=650)

    def test_that_a_negative_price_in_cost_raises_value_error(self):
        dispenser = MultiFuelDispenser()
        with self.assertRaises(ValueError):
            dispenser.cost(liters=4, price=-650)

    def test_that_dispense_returns_a_transaction(self):  # new
        dispenser = MultiFuelDispenser(fuel_type='petrol', liters=4)
        sale = dispenser.dispense()
        self.assertEqual(sale.total, 2600)


if __name__ == '__main__':
    unittest.main()