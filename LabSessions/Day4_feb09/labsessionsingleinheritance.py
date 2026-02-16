# Parent Class
class SavingsAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)


# Child Class (inherits SavingsAccount)
class InterestAccount(SavingsAccount):
    def addInterest(self, rate):
        interest = (self.balance * rate) / 100
        self.balance += interest
        print("Interest Added:", interest)


# Grand Child Class (Multilevel Inheritance)
class FinalAccount(InterestAccount):
    def display(self):
        print("Final Balance:", self.balance)


# Object Creation
acc = FinalAccount()
acc.deposit(10000)
acc.addInterest(5)
acc.display()