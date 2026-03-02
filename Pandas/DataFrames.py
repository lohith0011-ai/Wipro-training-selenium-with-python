import pandas as pd
# Create DataFrame from list of dictionaries
data = [
    {"Name": "Ram", "Age": "25"},
    {"Name": "Sam", "Age": "30"},
    {"Name": "John", "Age": "45"}
]

df = pd.DataFrame(data)
print(df)

# create Dataframe from dictionary of series
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

df = pd.DataFrame({"A": s1, "B": s2})
print(df)

# create dataframe from numpy array

import numpy as np

arr = np.array([[1,2],[3,4],[5,6]])
df = pd.DataFrame(arr, columns=["A", "B"])
print(df)

# create dataframe with custom index

dat = {
    "Name": ["Ram", "Sam"],
    "Age": [25, 30]
}

df = pd.DataFrame(data, index=["Emp1", "Emp2"])
print(df)