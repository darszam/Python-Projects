from BankAccounts.Models.AccountHolder import AccountHolder
from BankAccounts.Models.Account import Account
from BankAccounts.Models.Timezone import Timezone

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