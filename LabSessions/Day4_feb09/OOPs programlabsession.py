import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example
c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())




from datetime import date

class Person:
    def __init__(self, name, country, dob):  # dob in YYYY-MM-DD
        self.name = name
        self.country = country
        self.dob = dob

    def age(self):
        birth_year = int(self.dob.split("-")[0])
        current_year = date.today().year
        return current_year - birth_year


# Example
p = Person("Rahul", "India", "2000-05-10")
print("Age:", p.age())




import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Example
sq = Square(4)
print("Square Area:", sq.area())
print("Square Perimeter:", sq.perimeter())




class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)


class Bus(Vehicle):
    pass


# Example
b = Bus("Volvo", 80)
b.show()




class Vehicle:
    pass


# Example
v = Vehicle()
print(v)