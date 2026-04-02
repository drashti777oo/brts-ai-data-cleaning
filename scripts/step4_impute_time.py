import pandas as pd

print("Loading cleaned data...")

df = pd.read_csv("../output/cleaned_brts.csv")

print("Missing before:")

print("InsertTime:",df['InsertTime'].isnull().sum())
print("UpdatedTime:",df['UpdatedTime'].isnull().sum())

# Fill InsertTime from GPSTime
df['InsertTime'] = df['InsertTime'].fillna(df['GPSTime'])

# Fill UpdatedTime from GPSTime
df['UpdatedTime'] = df['UpdatedTime'].fillna(df['GPSTime'])

print("\nMissing after:")

print("InsertTime:",df['InsertTime'].isnull().sum())
print("UpdatedTime:",df['UpdatedTime'].isnull().sum())

# Save result
df.to_csv("../output/time_fixed_brts.csv",index=False)

print("\nTime imputation complete")