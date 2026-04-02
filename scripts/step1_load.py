import pandas as pd

# File paths
file1 = "../raw_data/jbm1 16-20.csv"
file2 = "../raw_data/jbm2 16-20.csv"

print("Loading datasets...")

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

print("Dataset 1 shape:", df1.shape)
print("Dataset 2 shape:", df2.shape)

# Combine datasets
df = pd.concat([df1, df2], ignore_index=True)

print("\nCombined dataset shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Info:")
print(df.info())

print("\nFirst rows:")
print(df.head())