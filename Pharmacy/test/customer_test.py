import unittest

from customer import Customer
from user import User


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Ada", "0801")

    def test_customer_is_a_user(self):
        self.assertIsInstance(self.customer, User)

    def test_customer_is_created_with_given_values(self):
        self.assertEqual(self.customer.name, "Ada")
        self.assertEqual(self.customer.phone_number, "0801")

    def test_id_is_none_by_default(self):
        self.assertIsNone(self.customer.id)

    def test_cart_is_empty_by_default(self):
        self.assertEqual(self.customer._cart, {})

    def test_can_check_name(self):
        self.customer.name = "Bola"
        self.assertEqual(self.customer.name, "Bola")

    def test_can_check_phone_number(self):
        self.customer.phone_number = "0909"
        self.assertEqual(self.customer.phone_number, "0909")

    def test_can_set_id(self):
        self.customer.id = 7
        self.assertEqual(self.customer.id, 7)

if __name__ == "__main__":
    unittest.main()