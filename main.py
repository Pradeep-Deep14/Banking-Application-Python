#Banking Applications

class Account:
    def __init__(self,account_no,balance=0):
        self.account_no=account_no
        self.balance=balance

#Method 1 Debit Method
    def debit(self,amount):
        self.balance -= amount
        print(f"Your account is being debited by {amount}")
        print(f"Your account balance is {self.balance}")

#Method 2 Credit Method
    def credit(self,amount):
        self.balance +=amount
        print(f"Your account is being credited by {amount}")
        print(f"Your account balance is {self.balance}")

    def get_balance(self):
        print(f"Yout account balance is {self.balance}")

#Objects or Instances

Acc1=Account(101,15000)
Acc2=Account(102,5000)
Acc3=Account(103,11000)

#Transactions
#Checking Balance

Acc1.get_balance()

#Debit 10000 and Credit 2000

Acc1.debit(10000)
Acc1.credit(2000)
Acc1.get_balance()

#Checking Balance

Acc2.get_balance()