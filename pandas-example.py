import pandas as pd

# Pandas is a library, which is used to handle and manipulate tabular data efficiently
# It provides powerful data structures like DataFrame, which is like an in-memory spreadsheet

# Create a DataFrame using a dictionary
data = {
    'Name': ['Ganesh', 'Balayya', 'NTR', 'Keerthy Suresh'],
    'Age': [24, 62, 41, 32],
    'City': ['Vijayawada', 'Hyderabad', 'Nimmakuru', 'Chennai']
}

# Create a DataFrame object from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Pandas allows easy manipulation of data, for example, filtering rows
# Filtering people older than 25
older_than_25 = df[df['Age'] > 25]

# Display filtered DataFrame
print("\nPeople older than 25:")
print(older_than_25)
