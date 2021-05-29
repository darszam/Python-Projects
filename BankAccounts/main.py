from BankAccounts.AccountHolder import AccountHolder
from BankAccounts.Account import Account

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