class Bank_account:
    def __init__(self, balance=0, interest_rate=0.01):
        self.account_balance = balance
        self.interest_rate = interest_rate

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    # takes an argument that is the amount of the withdrawal
    def make_withdrawal(self, amount):
    	# the specific user's account decreases by the amount of the value received
        if (amount > self.account_balance):
            print("Insufficient funds: Charging a $5 fee!")
            self.account_balance -= 5
        self.account_balance -= amount
        return self

    def display_account_balance(self):
        print("The account balance is :", self.account_balance)
        return self

    def yield_interest(self):
        self.account_balance = self.account_balance * (1+self.interest_rate)
        return self

account_guido = Bank_account(100,0.01)
account_tina = Bank_account(200,0.02)

account_guido.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50).yield_interest().display_account_balance()
account_tina.make_deposit(200).make_deposit(200).make_withdrawal(30).make_withdrawal(40).make_withdrawal(50).make_withdrawal(50).yield_interest().display_account_balance()