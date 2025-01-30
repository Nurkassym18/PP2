class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self):
        k=int(input())
        self.balance+=k
        print(self.balance)
    def withdraw(self):
        l=int(input())
        if(l>self.balance):
            print("No enough money")
        self.balance-=l
        print(self.balance)



money = Account("Nurkassym",18000)
money.deposit()
money.withdraw()