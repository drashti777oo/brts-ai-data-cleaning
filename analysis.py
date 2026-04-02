import pandas as pd

file = "jbm1 16-20.csv"

df = pd.read_csv(file, nrows=1000)

print("Columns:")
print(df.columns)

print("\nMissing values:")
print(df.isnull().sum())

print("\nShape:")
print(df.shape)