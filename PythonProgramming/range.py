# all numbers should be integers
# step size cannot be zero

a=range(5)
print(a[1])
print(a[4])

a1 = range(2,6)
print(a1[2])

# for loop for range of  3 arguments
a = range(2,6,4)
for i in a:
    print(i)

# for loop for range of negative  3 arguments
a= range(2,15,-3)
for i in a:
    print(i)

    a = range(15,2,-1)
    for i in a:
        print(i)

    #Scenario : Allow 3 login attempts
    for attempt in range(3):
        pin
    if pin == "1234":
        print("Access granted")
        break
    else:
        print("Try again")

 #Scenario: Apply discount based on the position (index) of the item
 prices = [100,200,300,400]
 for i in range(len(prices)):
     if i % 2 == 0:
         print("Discount applied on item{1}")

#Scenario : simulate polling every second for 10 seconds

import time

for second in range(10):
    print("Checking the status at {second} sec ")
    time.sleep(1)

# accessing of the enumerate values

a=['god', 'is', 'great']
b=enumerate(a)
nxt_val=next(b)
print(nxt_val)
