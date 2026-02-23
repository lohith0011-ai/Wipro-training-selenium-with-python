students={
    101:"ravi",
    102:"anjali",
    103:"suresh"
}
print(students)

print(students[101])

print(students.get(105,"key not found"))

students[102]="ananya"
print(students)

del students[103]
print(students)

students.pop(101)
print(students)

print(len(students))

print(students.keys())

print(students.values())

print(students.items())