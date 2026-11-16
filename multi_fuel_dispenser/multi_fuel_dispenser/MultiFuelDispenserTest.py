import unittest

import multi_fuel_dispenser
from multi_fuel_dispenser.MultiFuelDispenser import MultiFuelDispenser

class MultiFuelDispenserTest(unittest.TestCase):

    def test_that_the_filling_station_have_the_petrol_and_it_price(self):
        multi_fuel_dispenser = MultiFuelDispenser(fuel_type= 'petrol')
        result = multi_fuel_dispenser.get_fuel_price()
        self.assertEqual(result,650)

    def test_that_the_filling_station_have_the_kerosene_and_it_price(self):
        multiFuelDispenser = MultiFuelDispenser(fuel_type= 'Kerosene')
        result = multiFuelDispenser.get_fuel_price()
        self.assertEqual(result,550)

    def test_that_the_filling_station_have_the_diesel_and_it_price_even_if_it_written_in_lower_case(self):
        multiFuelDispenser = MultiFuelDispenser(fuel_type= 'Diesel')
        result = multiFuelDispenser.get_fuel_price()
        self.assertEqual(result,720)

    def test_invalid_fuel_type_raises_value_error(self):
        multiFuelDispenser = MultiFuelDispenser(fuel_type='rocket fuel')
        self.assertRaises(ValueError, multiFuelDispenser.get_fuel_price)

    def test_that_if_the_liter_is_not_specified_the_price_can_be_use_to_get_Liter(self):
        multiFuelDispenser = MultiFuelDispenser(fuel_type= 'petrol', fuel_price= 650)
        result = multiFuelDispenser.calculate_fuel_price(3000)
        self.assertEqual(round(result, 2),4.62)

    def test_that_when_price_is_not_specified_and_liter_is_specified_it_should_still_show_price(self):
        multiFuelDispenser = MultiFuelDispenser(fuel_type= 'petrol', fuel_price=650)
        result = multiFuelDispenser.calculate_liters(4)
        self.assertEqual(round(result, 2), 2600)

    def test_that_when_a_client_buys_petrol_is_total_bill_is_shown(self):
        multiFuelDispenser = MultiFuelDispenser()
        result = multiFuelDispenser.calculate_fuel_cost(liter=4, price=650)
        self.assertEqual(round(result, 2), 2600)

    # def test_that_when_a_client_buys_petrol_is_total_bill_is_shown_not_as_negative(self):
    #     multiFuelDispenser = MultiFuelDispenser
    #     self.assertRaises(ValueError, multiFuelDispenser.cost(()


