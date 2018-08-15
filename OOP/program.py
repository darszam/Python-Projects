from AccountBusiness import AccountBusiness
from AccountChecking import AccountChecking
from AccountSaving import AccountSaving
#Each account constructor has first customer identifier which is linked to the person. Simmons has two accounts but one customer id
smith_checking = AccountChecking(1,1234.42)
snake_business = AccountBusiness(2,2345.75)
simmons_saving = AccountSaving(4,5321.53)
simmons_business = AccountBusiness(4,2343.56)

#bank list contains bank accounts in a list that is made in template [Account,customer identifier, type of account]
# 1 for Checking, 2 for Saving, 3 for Business
bank_list = [[smith_checking,1,1],[snake_business,2,3],[simmons_saving,4,2],[simmons_business,4,3]]
answer = "y"
while(answer != "exit"):
    print("Welcome to the Python Bank!")
    print("Type 1 to enter bank menu")
    print("Type exit to exit the program")
    print()
    answer = input("")
    if(answer=="1"):
        answer = int(input("Enter the customer identifier:"))
        customer_accounts = []
        customer_accounts_id = []
        for account in bank_list:
            if(account[1]==answer):
                customer_accounts.append(account)
                customer_accounts_id.append(account[2])
        if(len(customer_accounts)==0):
            print("There is no customer with that identifier")
        if(len(customer_accounts)>0):
            print("Which account would you like to check?")
            print()
            answer = int(input("Type: 1 for Checking account, 2 for Saving account, 3 for Business account"))
            if(answer in customer_accounts_id):
                for cust_account in customer_accounts:
                    if(answer == cust_account[2]):
                        active_account = cust_account
                while(answer!=4):
                    print("What do you want to do?")
                    print("1) Show bilance")
                    print("2) Deposit money")
                    print("3) Withdraw money")
                    print("4) Exit")
                    print()
                    answer = int(input("Type your choice"))
                    if(answer == 1):
                        active_account[0].printBilance()
                    if(answer == 2):
                        print("How much do you want to deposit?")
                        print()
                        answer = input("Type amount")
                        active_account[0].deposit(answer)
                    if(answer == 3):
                        print("How much do you want to withdraw?")
                        print()
                        answer = input("Type amount")
                        active_account[0].withdraw(answer)
            else:
                print("There is no such account!")

    else:
        answer="exit"

print("Thank you for using new Python Bank ATM!")
