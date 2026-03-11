import matplotlib.pyplot as plt
import pandas as pd
x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.plot(x,y)
# x axis label
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Simple Plot')

# show method will display the data
plt.show()

# Simple data
subjects = ["Maths", "Science", "English", "History", "Computer"]
marks = [85, 75, 95, 55, 92]

# creates the line graph
plt.plot(subjects, marks)

plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Student Marks')
plt.show()


# matplotlib with pandas integration

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 150, 200, 250 ,220]
}

df = pd.DataFrame(data)

plt.plot(df["Month"], df["Sales"])

plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales')
plt.show()

