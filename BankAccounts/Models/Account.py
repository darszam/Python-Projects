import datetime
import decimal

from BankAccounts.Models.AccountHolder import AccountHolder
from BankAccounts.Models.Timezone import Timezone


class Account:
    _monthly_interest_rate = decimal.Decimal(0.5)
    _transaction_number = 0
    format_date = '%Y%m%d%H%M%S'

    class Confirmation:
        def __init__(self, confirmation: str, timezone: Timezone):
            # confirmation template "[D,W,I,X]-{account_number}-{utc time}-{transaction_number}"
            confirmation_tokens = confirmation.split('-')
            self.account_number = confirmation_tokens[1]
            self.transaction_code = confirmation_tokens[0]
            self.time_utc = datetime.datetime.strptime(confirmation_tokens[2], Account.format_date)
            self.time = datetime.datetime.strptime(confirmation_tokens[2], Account.format_date) + timezone.offset
            self.transaction_number = confirmation_tokens[3]

        @property
        def account_number(self):
            return self._account_number

        @property
        def transaction_code(self):
            return self._transaction_code

        @property
        def time_utc(self):
            return self._time_utc

        @property
        def time(self):
            return self._time

        @property
        def transaction_number(self):
            return self._transaction_number

        @account_number.setter
        def account_number(self, value):
            self._account_number = value

        @transaction_code.setter
        def transaction_code(self, value):
            self._transaction_code = value

        @time_utc.setter
        def time_utc(self, value):
            self._time_utc = value

        @time.setter
        def time(self, value):
            self._time = value

        @transaction_number.setter
        def transaction_number(self, value):
            self._transaction_number = value

        def __repr__(self):
            return f"{self.account_number}, {self.transaction_code}, {self.transaction_number}, {self.time_utc}, {self.time}"

    @classmethod
    def get_monthly_interest_rate(cls):
        return cls._monthly_interest_rate

    @classmethod
    def get_transaction_number(cls):
        return cls._transaction_number

    @classmethod
    def increment_transaction_number(cls):
        cls._transaction_number += 1

    @classmethod
    def set_monthly_interest_rate(cls, value: decimal.Decimal):
        cls._monthly_interest_rate = value

    def __init__(self, acc_num: int, holder: AccountHolder, balance: decimal.Decimal, timezone: Timezone):
        self.acc_number = acc_num
        self.acc_holder = AccountHolder(holder.first_name, holder.last_name)
        self._balance = balance
        self._timezone = timezone

    @property
    def acc_number(self):
        return self._acc_number

    @property
    def acc_holder(self):
        return self._acc_holder

    @property
    def balance(self):
        return self._balance

    @property
    def timezone(self):
        return self._timezone

    @acc_number.setter
    def acc_number(self, value: int):
        self._acc_number = value

    @acc_holder.setter
    def acc_holder(self, value: AccountHolder):
        self._acc_holder = value

    @balance.setter
    def balance(self, value: int):
        raise ValueError("Can't modify balance, please use withdraw/deposit methods")

    def __repr__(self):
        return f"Account_id: {self.acc_number}, Account Holder: {self.acc_holder}, Balance: {self.balance}, Interest " \
               f"Rate: {Account.get_monthly_interest_rate()} "

    def withdraw(self, value: decimal.Decimal):
        if self.balance - value < 0:
            print("Insufficient funds. Transaction canceled.")
            confirmation = f"X-{self.acc_number}-{datetime.datetime.utcnow().strftime(Account.format_date)}-{Account.get_transaction_number()}"
            Account.increment_transaction_number()
            return confirmation
        else:
            self._balance -= value
            print(f"Balance after withdraw: {self.balance}")
            confirmation = f"W-{self.acc_number}-{datetime.datetime.utcnow().strftime(Account.format_date)}-{Account.get_transaction_number()}"
            Account.increment_transaction_number()
            return confirmation

    def deposit(self, value: decimal.Decimal):
        self._balance += value
        print(f"Balance after deposit: {self.balance}")
        confirmation = f"D-{self.acc_number}-{datetime.datetime.utcnow().strftime(Account.format_date)}-{Account.get_transaction_number()}"
        Account.increment_transaction_number()
        return confirmation

    def interest_deposit(self):
        self._balance *= Account.get_monthly_interest_rate()
        confirmation = f"I-{self.acc_number}-{datetime.datetime.utcnow().strftime(Account.format_date)}-{Account.get_transaction_number()}"
        Account.increment_transaction_number()
        return confirmation

    @staticmethod
    def get_confirmation(confirmation: str, timezone: Timezone):
        confirmation_object = Account.Confirmation(confirmation, timezone)
        return confirmation_object
