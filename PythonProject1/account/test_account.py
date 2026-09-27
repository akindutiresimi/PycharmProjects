import unittest

from account.account import Account
class MyTestCase(unittest.TestCase):

    def test_that_account_can_be_created(self):
        acc = Account("winifred")
        self.assertEqual(acc.balance, 0)
        self.assertEqual(acc.name, "winifred")

    def test_that_account_can_receeive_deposit(self):
        acc = Account("winifred")
        acc.deposit(2500)
        self.assertEqual(acc.balance, 2500)

    def test_that_account_can_not_receive_amount_for_deposit(self):
        acc = Account("winifred")
        self.assertRaises(ValueError, acc.deposit, -2500)

    def test_that_account_can_be_withdraw_from(self):
        acc = Account("winifred")
        acc.deposit(2500)
        acc.withdraw(2000)
        self.assertEqual(acc.balance, 500)

    def test_that_account_can_not_withdraw_negative_amount_for_withdraw(self):
        acc = Account("winifred")
        acc.deposit(5000)
        acc.withdraw(-500)
        self.assertEqual(acc.balance, 5500)

    def test_that_account_can_not_withdraw_amount_greater_Than_balance(self):
        acc = Account("winifred")
        acc.deposit(5000)
        self.assertRaises(ValueError, acc.withdraw,5500)


if __name__ == '__main__':
    unittest.main()



