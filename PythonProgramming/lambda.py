#filter + ve numbers
nums = [-5, 10, -3, 7, 0, 2]
pos = list(filter(lambda n: n>=0, nums))
print(pos)

#Filter non-empty strings
data = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda d: d!="", data))
print(non_empty)