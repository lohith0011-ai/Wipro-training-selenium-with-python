data = [(1, 3), (4, 1), (2, 2), (5, 0)]

sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)

sorted_data = sorted(data, key=lambda x: x[0])
print(sorted_data)





from datetime import datetime

dt = datetime.now()

get_year  = lambda d: d.year
get_month = lambda d: d.month
get_day   = lambda d: d.day
get_time  = lambda d: d.strftime("%H:%M:%S")

print("Year :", get_year(dt))
print("Month:", get_month(dt))
print("Date :", get_day(dt))
print("Time :", get_time(dt))




dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}

new_dict = {**dict1, **dict2, **dict3}
print(new_dict)