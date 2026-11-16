import unittest

from admin import Admin
from user import User


class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.admin = Admin("Semi", 1, "08012345678")

    def test_admin_is_a_user(self):
        self.assertIsInstance(self.admin, User)

    def test_can_check_name(self):
        self.admin.name = "Tolu"
        self.assertEqual(self.admin.name, "Tolu")

    def test_can_check_phone_number(self):
        self.admin.phone_number = "09099999999"
        self.assertEqual(self.admin.phone_number, "09099999999")

    def test_can_check_id(self):
        self.admin.id = 42
        self.assertEqual(self.admin.id, 42)

if __name__ == "__main__":
    unittest.main()

