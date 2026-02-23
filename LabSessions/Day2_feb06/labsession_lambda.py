nums = [1, 2, 3, 4, 5, 6]

from functools import reduce

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))

# Square them
squares = list(map(lambda x: x * x, evens))

# Find their sum
total = reduce(lambda x, y: x + y, squares)

print("Even numbers:", evens)
print("Squared values:", squares)
print("Sum:", total)


salaries = [25000, 40000, 32000, 18000]

from functools import reduce

# Filter salaries > 30000
eligible = list(filter(lambda x: x > 30000, salaries))

# Add 10% hike
hiked = list(map(lambda x: x + (x * 0.10), eligible))

# Find total payout
total_payout = reduce(lambda x, y: x + y, hiked)

print("Eligible salaries:", eligible)
print("After 10% hike:", hiked)
print("Total payout:", total_payout)