import pandas as pd

# Create a DataFrame containing missing (None/NaN) values.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, None, 30, 28, None],
    'Salary': [50000, 60000, None, 45000, 70000],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR'],
    'City': ['Bangalore', 'Mumbai', 'Bangalore', 'Delhi', 'Bangalore']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)


# Detect missing values using appropriate function
print("\nMissing Values (True indicates missing):")
print(df.isnull())

print("\nCount of Missing Values per Column:")
print(df.isnull().sum())


# Replace missing values with 0.
df_filled = df.fillna(0)
print("\nDataFrame after replacing missing values with 0:")
print(df_filled)


# Drop rows containing missing values.
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)


# Sort the DataFrame by Age in ascending order.
df_sorted_age = df.sort_values(by='Age', ascending=True)
print("\nSorted by Age (Ascending):")
print(df_sorted_age)


# Sort the DataFrame by Salary in descending order.
df_sorted_salary = df.sort_values(by='Salary', ascending=False)
print("\nSorted by Salary (Descending):")
print(df_sorted_salary)


# Perform groupby on Department and find average Salary per department.
avg_salary = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary per Department:")
print(avg_salary)


# Find total Salary per department using group by.
total_salary = df.groupby('Department')['Salary'].sum()
print("\nTotal Salary per Department:")
print(total_salary)


# Filter employees where Age > 25 AND City = 'Bangalore'
filtered = df[(df['Age'] > 25) & (df['City'] == 'Bangalore')]
print("\nEmployees with Age > 25 and City = Bangalore:")
print(filtered)


# Create a new column 'Tax' which is 10% of Salary using apply().
df['Tax'] = df['Salary'].apply(lambda x: x * 0.10 if pd.notnull(x) else x)
print("\nDataFrame with Tax column (10% of Salary):")
print(df)