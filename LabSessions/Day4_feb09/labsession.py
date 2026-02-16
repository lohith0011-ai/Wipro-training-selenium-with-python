class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("--------------------")


# Creating 3 book objects
book1 = Book("Python Basics", "Guido van Rossum")
book2 = Book("Learning Java", "James Gosling")
book3 = Book("C Programming", "Dennis Ritchie")

# Printing details
book1.display()
book2.display()
book3.display()









class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
        self.perimeter = 2 * (length + width)

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area:", self.area)
        print("Perimeter:", self.perimeter)


# Creating object
rect1 = Rectangle(10, 5)

# Printing details
rect1.display()