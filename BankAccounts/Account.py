from BankAccounts.AccountHolder import AccountHolder
import decimal

class Account:
    _monthly_interest_rate = decimal.Decimal(0.5)

    @classmethod
    def get_monthly_interest_rate(cls):
        return cls._monthly_interest_rate

    @classmethod
    def set_monthly_interest_rate(cls, value: decimal.Decimal):
        cls._monthly_interest_rate = value

    def __init__(self, acc_num: int, holder_first_name: str, holder_last_name: str, balance: decimal.Decimal):
        self.acc_number = acc_num
        self.acc_holder = AccountHolder(holder_first_name, holder_last_name)
        self._balance = balance

    @property
    def acc_number(self):
        return self._acc_number

    @property
    def acc_holder(self):
        return self._acc_holder

    @property
    def balance(self):
        return self._balance

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
            raise ValueError("Insufficient funds. Transaction canceled.")
        else:
            self._balance -= value
            print(f"Balance after withdraw: {self.balance}")

    def deposit(self, value: decimal.Decimal):
        self._balance += value
        print(f"Balance after deposit: {self.balance}")

