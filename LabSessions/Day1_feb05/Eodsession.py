#[1,2,3,4,5,6,7,8,9]
a=[1,2,3,4,5,6,7,8,9]
b=len(a)
c=0
for i in range(1,b):
    if a[i]>c:
print(c)

# remove the even numbers from the list

numbers=[1,2,3,4,5,6,7,8,9,10]
a=[]
for i in numbers:
    if i%2!=0:
        a=a+[i]
print(a)

# multiply the  items in the list
numbers = [1,2,3,4,5,6,7,8,9,10]
a=1
for i in numbers:
    a*=i
print(a)
