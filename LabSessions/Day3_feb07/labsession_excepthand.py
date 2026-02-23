try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter only numbers.")




import random
import string
char = random.choice(string.ascii_letters)
print("Random character:", char)


import random
import string

result = ""
for i in range(5):
    result += random.choice(string.ascii_letters)

print("Random string:", result)


import random
import string

length = 8
fixed_string = ''.join(random.choice(string.ascii_letters) for i in range(length))

print("Fixed length string:", fixed_string)