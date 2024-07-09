class Account():
    def __init__(self, owner, balance=0):
       
       #Attributes
        self.owner = owner
        self.balance = balance
    
    #Methods
    def deposit(self, dep):
        self.balance += dep
        print(f"{dep} has been deposited to your account.")

    def withdraw(self, withd):
        if withd <= self.balance:
            self.balance -= withd
            print(f"{withd} successful withdrawal.")
        else:
            print("Funds Unavailable! ")
    
    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: ${self.balance}"