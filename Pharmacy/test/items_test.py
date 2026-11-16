import unittest
from datetime import date

from items import Item


class TestItem(unittest.TestCase):
    def setUp(self):
        self.expiry = date(2027, 1, 1)
        self.item = Item("Bandage", self.expiry, 100, 5)


    def test_item_is_created_with_given_values(self):
        self.assertEqual(self.item.name, "Bandage")
        self.assertEqual(self.item.expiry_date, self.expiry)
        self.assertEqual(self.item.price, 100)
        self.assertEqual(self.item.quantity, 5)


    def test_zero_quantity_is_allowed(self):
        item = Item("Sold out", self.expiry, 10, 0)
        self.assertEqual(item.quantity, 0)


    def test_negative_price_on_creation_raises(self):
        with self.assertRaises(ValueError) as ctx:
            Item("Bad", self.expiry, -1)
        self.assertEqual(str(ctx.exception), "Price cannot be negative")


    def test_can_change_price(self):
        self.item.price = 250
        self.assertEqual(self.item.price, 250)


if __name__ == "__main__":
    unittest.main()