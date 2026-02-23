#^\d+$

import re

text = "12345"
result = re.fullmatch(r"\d+", text)

print("Valid" if result else "Invalid")

#[a-z]

text = "Hello World"
result = re.findall(r"[a-z]", text)

print(result)

#[A-Z]

text = "Hello World PYTHON"
result = re.findall(r"[A-Z]", text)

print(result)

#^Hello

text = "Hello everyone"
print(bool(re.match(r"^Hello", text)))

#world$

text = "Hello world"
print(bool(re.search(r"world$", text)))

#\w+

text = "Python is very powerful"
result = re.findall(r"\w+", text)

print(result)

#^.{5}$

text = "Hello"
print(bool(re.fullmatch(r".{5}", text)))


#python

text = "python is fun. Python is powerful. python!"
result = re.findall(r"python", text)

print(result)


#\s

text = "Python is easy to learn"
result = re.sub(r"\s", "_", text)

print(result)