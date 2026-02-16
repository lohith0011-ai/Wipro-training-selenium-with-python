import csv

# reading the csv file
with open("/DataFormats/data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# writing to the csv file
with open("/DataFormats/writecsv.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id","name","marks"])
    writer.writerow([1, "rahul", 85])
    writer.writerow([2, "anita",90])


# append ding the data to csv file
with open("/DataFormats/data.csv", "a", newline="")as file:
    writer = csv.writer(file)
    writer.writerow([3,"kiran",88])