# expections - runtime errors which will disrupt the norma; program flow
# benefits
# helps in debugging
# prevents program crashing
# handling errors and exceptions in the code more effocioently

# try except

# try - code tp be executed
# except - exceptions details catching
#else: if the exception does not occur than else part will be executed
# finally - mandated code
# custom exceptions

try:
    a = int(input("Enter the number"))
    b = int(input("Enter the number"))
    print(a/b)
except ZeroDivisionError:
        print("cannot divide by zero")
except ValueError:
        print("Please enter valid numbers")
# generic exception
try:
    a = 10/2
except Exception as e:
    print(e)
# runs only if no exception occurs
else:
    print("Divison successfull")
# mandatory code
finally:
    print("Close the browser")
# custom exceptions - creating a own exception
age = int(input("Enter the age"))
if age < 18:
    raise ValueError("Age must be 18 or above")
