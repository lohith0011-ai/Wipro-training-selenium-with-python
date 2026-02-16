class OneToFive:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

# Usage
obj = OneToFive()
for i in obj:
    print(i)




class EvenNumbers:
    def __init__(self, limit):
        self.num = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        if self.num <= self.limit:
            return self.num
        else:
            raise StopIteration

# Usage
even = EvenNumbers(10)
for i in even:
    print(i)




class Demo:
    def __init__(self):
        self.x = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.x <= 3:
            val = self.x
            self.x += 1
            return val
        else:
            raise StopIteration

d = Demo()
print(next(d))
print(next(d))
print(next(d))




def numbers(n):
    for i in range(1, n + 1):
        yield i

for num in numbers(5):
    print(num)




def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

for e in even_numbers(10):
    print(e)




def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for f in fibonacci(6):
    print(f)




def retry():
    attempts = 1
    while attempts <= 3:
        yield f"Attempt {attempts}"
        attempts += 1

for r in retry():
    print(r)





