import pandas as pd

df = pd.read_csv("../output/cleaned_brts.csv")

print("Missing InsertTime:",df['InsertTime'].isnull().sum())

print("Missing GPSTime:",df['GPSTime'].isnull().sum())

print("Missing UpdatedTime:",df['UpdatedTime'].isnull().sum())