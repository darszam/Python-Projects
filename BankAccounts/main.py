from BankAccounts.AccountHolder import AccountHolder
from BankAccounts.Account import Account
from BankAccounts.Timezone import Timezone
import datetime

first = AccountHolder("John", "Smith")
print(first)
tz1 = Timezone("First", 2, 17)
print(tz1)

f_account = Account(1234, first, 100, tz1)


conf = f_account.withdraw(20)
print(conf)
print(f_account)

conf = f_account.withdraw(30)
print(conf)
print(f_account)

c1 = Account.get_confirmation(conf, tz1)

print(c1)