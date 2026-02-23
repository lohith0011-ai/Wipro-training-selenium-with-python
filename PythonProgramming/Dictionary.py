# dictionary items - key value
# similar to list and tuples
# for integers, tuples and strings - keys must be immutable
# list cannot be used in the key for dictionary as it is mutable in nature


country = {
    "india":"delhi",
    "canada":"ottawa",
    "england":"london"
}

print(country)
# access the values







# remove elements
del country["india"]
print(country)

# clear
#country.clear()










# for integers keys must be immutable

# integer as a key
my_dict = {1:"one", 2:"two", 3:"three"}
print(my_dict)

my_dict={1:"four", 2:"two",3:"three",1:"one"}
print(my_dict)

# for integers keys must be immutable

# tuples as a key
my_dict={(1,2):"one two",3:"three"}

my_dict={(1,2):"one two",3:"three",3:"four"}
print(my_dict)

# list as key
my_dict={1:"hello",[1,2]:"there you"}
print(my_dict)

# pop-removes the item with spec key
my_dict={1:"one",2:"two",3:"three"}
print(my_dict)

my_dict.pop(2)
print(my_dict)

# update() - adds or changes the dict
my_dict={1:"one",2:"two",3:"three"}
print(my_dict)

my_dict.update({4:"four"})
print(my_dict)


# keys()
my_dict={1:"one",2:"two",3:"three"}
print(my_dict.keys())

# values()
my_dict={1:"one",2:"two",3:"three"}
print(my_dict.values())

# popitem() return the last inserted keyword
my_dict={1:"one",2:"two",3:"three"}
print(my_dict)

print(my_dict.popitem())
print(my_dict)

# copy returns the copy of dist
my_dict={1:"one",2:"two",3:"three"}
print(my_dict)

new_dict=my_dict.copy()
print(new_dict)

# dict inside the list

employees= {
    {"id":1,"name": "lohith", "role":"kp"},
    {"id":2,"name":"uday","role":"up"},
    {"id":3,"name":"kumar","role":"au"}
}

print(employees[0])
print(employees[0]["name"])

for emp in employees:
    print(emp["name"], emp["role"])

employees.append({"id":4, "name":"vasu","role":"as"})
print(employees)

employees.pop(0)
print(employees)

# search a item in the list
for emp in employees:
    if emp["name"]=="lohtih":
        print(emp)