import sys
from bank_account import Bank_account

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.account_balance = 0
        self.account = Bank_account(balance=0, interest_rate=0.02)
    # adding the deposit method
    def make_deposit(self,amount):
        # self.account_balance += amount
        self.account.account_balance += amount
        return self
    

    def make_withdrawal(self,amount):# takes an argument that is the amount of the withdrawal
    	# the specific user's account decreases by the amount of the value received
        if (amount > self.account.account_balance):
            print("There is not enough money in this account to withdraw!")
            return False
        self.account.account_balance -= amount
        return self

    # def make_deposit(self,amount):  
    # 	self.account_balance += amount
    #     return self
   
    def display_user_balance(self):
        print("The account balance is :",self.account.account_balance)
        return self
    
    def transfer_money(self,other_user,amount):
        if (amount > self.account.account_balance):
            print("There is not enough money in ther account to transfer！")
            return False
        self.account.account_balance -= amount
        other_user.account.account_balance += amount
        return self



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
tina = User("Tina Graham","tina@python.com")
# guido.make_deposit(100)
# guido.make_deposit(100)
# guido.make_deposit(200)
# guido.make_withdrawal(50)
# guido.display_user_balance()
guido.make_deposit(100).make_deposit(100).make_deposit(200).make_withdrawal(50).display_user_balance()
# monty.make_deposit(50)
# monty.make_deposit(300)
# monty.make_withdrawal(100)
# monty.make_withdrawal(400)
# monty.display_user_balance()
monty.make_deposit(50).make_deposit(300).make_withdrawal(100).make_withdrawal(100).display_user_balance()
# tina.make_deposit(200)
# tina.make_withdrawal(20)
# tina.make_withdrawal(50)
# tina.make_withdrawal(100)
# tina.display_user_balance()
tina.make_deposit(200).make_withdrawal(20).make_withdrawal(50).make_withdrawal(100).display_user_balance()
# guido.transfer_money(tina,30)
# guido.display_user_balance()
guido.transfer_money(tina, 30).display_user_balance()
tina.display_user_balance()
