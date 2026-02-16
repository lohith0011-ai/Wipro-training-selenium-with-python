def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

nums = [10, 20, 30, 40]
result = sum_list(nums)
print(result)


def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

x = 15
y = 42
z = 27

result = max_of_three(x, y, z)
print(result)