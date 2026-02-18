class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")



c1 = Car("Toyota", "Innova", 2000000)
c1.display()





class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"



s1 = Student("Lohith", 82)
print("Grade:", s1.get_grade())





class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)



acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()





class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(self.name, self.emp_id, self.salary)


e1 = Employee("John", 101, 50000)
e1.display()





class Counter:
    count = 0   # class variable

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Objects created:", cls.count)


# Example
a = Counter()
b = Counter()
c = Counter()

Counter.show_count()





class Company:
    company_name = "Tech Solutions"   # class variable

    def __init__(self, employee):
        self.employee = employee

    def display(self):
        print(self.employee, "works at", Company.company_name)



c1 = Company("Ravi")
c1.display()





class EmailValidator:

    @staticmethod
    def validate(email):
        if "@" in email and "." in email:
            return "Valid Email"
        return "Invalid Email"



print(EmailValidator.validate("test@gmail.com"))
print(EmailValidator.validate("wrongemail"))





class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):   # Inheriting Vehicle
    def ride(self):
        print("Bike is riding")


# Example
b = Bike()
b.start()   # from parent class
b.ride()    # from child class





class Person:
    def show_person(self):
        print("I am a person")

class Employee(Person):
    def show_employee(self):
        print("I am an employee")

class Manager(Employee):
    def show_manager(self):
        print("I am a manager")


# Example
m = Manager()
m.show_person()
m.show_employee()
m.show_manager()





class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()   # call parent method
        print("Child method")


# Example
c = Child()
c.show()





class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def show_balance(self):
        print("Balance:", self.__balance)


# Example
acc = BankAccount(1000)
acc.show_balance()




class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount")


# Example
acc = BankAccount(500)
print(acc.get_balance())

acc.set_balance(1500)
print(acc.get_balance())





class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative")
        else:
            self.__salary = value


# Example
e = Employee(30000)
print(e.salary)

e.salary = -5000   # not allowed
e.salary = 40000   # allowed

print(e.salary)





class Shape:
    def area(self):
        pass   # common method

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w



c = Circle(5)
r = Rectangle(4, 6)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())





class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c



calc = Calculator()

print(calc.add(5))        # 1 argument
print(calc.add(5, 10))    # 2 arguments
print(calc.add(5, 10, 15)) # 3 arguments





class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def show(self):
        print(self.value)



n1 = Number(10)
n2 = Number(20)

n3 = n1 + n2   # calls __add__()
n3.show()





class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()   # Engine object inside Car

    def start_car(self):
        self.engine.start()
        print("Car started")



c = Car()
c.start_car()





class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, players):
        self.players = players

    def show_players(self):
        for p in self.players:
            print(p.name)



p1 = Player("Ravi")
p2 = Player("Kumar")
p3 = Player("Arun")

team = Team([p1, p2, p3])
team.show_players()

