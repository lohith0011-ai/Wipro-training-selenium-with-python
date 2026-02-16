# operator polymorphism means
# the same operator behaves differently for diff data types or the objects
#+ add numbers
# + joins the strings
# + merges the lists
# operator overloading in python

# python
'''
__add__()
__sub__()
__mul__()
__eq__()
__lt__()
__gt__()
'''

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)

# now + will work for the custom objects