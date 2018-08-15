from account import Account
class AccountSaving(Account):
    def __init__(self, customer_id, deposit_money):
        Account.__init__(self,customer_id)        
        self.format_money = "{:.2f}".format(deposit_money)
        
        self.amount_whole = int(self.format_money[:self.format_money.find('.')])
        self.amount_part = int(self.format_money[self.format_money.find('.') + 1:])

    def printBilance(self):
        print("{}.{}".format(self.amount_whole,self.amount_part))

    def deposit(self, money):
        self.amount_whole += int(str(money)[:str(money).find('.')])
        self.amount_part += int(str(money)[str(money).find('.') + 1:])
        if(self.amount_part>100):
            self.amount_whole+=1
            self.amount_part-=100

    def withdraw(self, withdraw_amount):
        self.amount = "{:.2f}".format(float(withdraw_amount))
        self.withdraw_whole = int(self.amount[:self.amount.find('.')])
        self.withdraw_part = int(self.amount[self.amount.find('.')+1])

        if(self.amount_whole<self.withdraw_whole and self.amount_part < self.withdraw_part):
            print("Error! Bilance is smaller than withdraw amount")
        else:
            if(self.amount_part<self.withdraw_part):
                self.amount_part += 100
                self.amount_whole -= 1
                self.amount_part -= self.withdraw_part
            else:
                self.amount_part -= self.withdraw_part
            self.amount_whole -= self.withdraw_whole
