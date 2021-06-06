import unittest
import BankAccounts.Models.Account as Account
import BankAccounts.Models.AccountHolder as AccountHolder
import BankAccounts.Models.Timezone as Timezone


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.ac_holder = AccountHolder.AccountHolder("John", "Smith")
        self.tz1 = Timezone.Timezone("First", 2, 17)
        balance = 100
        account_number = 1234
        self.account = Account.Account(account_number, self.ac_holder, balance, self.tz1)

    def test_withdraw_transaction(self):
        # Testing when withdrawing amount smaller than balance
        amount_to_withdraw = 1 if self.account.balance > 1 else 0
        balance_before = self.account.balance
        confirmation = self.account.withdraw(amount_to_withdraw)
        confirmation_code = 'W'
        self.assertEqual(confirmation_code, confirmation[0])
        self.assertEqual(balance_before, amount_to_withdraw + self.account.balance)

        # Testing withdrawing amount greater than balance
        self.setUp()
        amount_to_withdraw = self.account.balance + 1
        balance_before = self.account.balance
        confirmation = self.account.withdraw(amount_to_withdraw)
        confirmation_code = 'X'
        self.assertEqual(confirmation_code, confirmation[0])
        self.assertEqual(balance_before, self.account.balance)


if __name__ == '__main__':
    unittest.main()
