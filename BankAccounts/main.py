from BankAccounts.AccountHolder import AccountHolder
from BankAccounts.Account import Account
from BankAccounts.Timezone import Timezone
import datetime

first = AccountHolder("John", "Smith")
print(first)

f_account = Account(1234, "John", "Smith", 100)

print(f_account)
Account.set_monthly_interest_rate(0.78)
print(f_account)

f_account.withdraw(20)
print(f_account)

f_account.deposit(30)
print(f_account)

try:
    f_account.withdraw(200)
    print(f_account)
except ValueError as e:
    print(e)

tz1 = Timezone("First", 2, 17)
print(tz1)

now = datetime.datetime.utcnow()
print(now)

print(now + tz1.offset)

try:
    tz_error = Timezone('        ', 0, 0)
except Exception as e:
    print(e)
