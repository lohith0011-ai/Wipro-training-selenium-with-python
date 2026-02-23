list(enumerate(['a','b','c']))


for  i, v in enumerate([10,20,30]):
    print(i,v)

colors=['red','green','blue']
for i, v in enumerate(colors, start=1):
     print(i,v)

list(enumerate("PYTHON",start=1))



nums=[10,20,30,40,50,60]
for i, v in enumerate(nums):
    if v==50:
        print(i)

for i, n in enumerate(range(10,60,10)):
    print(i,n)


for i, v in enumerate(data):
    print(i,v)


items=['a','b','c']
for i in enumerate(items):
    print(i)


list(enumerate([],start=5))
