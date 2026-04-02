import pandas as pd

file1 = "../raw_data/jbm1 16-20.csv"
file2 = "../raw_data/jbm2 16-20.csv"

print("Loading data...")

df1 = pd.read_csv(file1, low_memory=False)
df2 = pd.read_csv(file2, low_memory=False)

df = pd.concat([df1, df2], ignore_index=True)

print("\nDATASET SHAPE:")
print(df.shape)

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nZERO VALUES:")
for col in ['Speed','Latitude','Longitude','Heading']:
    print(col, (df[col] == 0).sum())

print("\nDUPLICATES:")
print(df.duplicated().sum())

print("\nSPEED STATS:")
print(df['Speed'].describe())

print("\nLATITUDE RANGE:")
print(df['Latitude'].min(), df['Latitude'].max())

print("\nLONGITUDE RANGE:")
print(df['Longitude'].min(), df['Longitude'].max())

print("\nTOTAL VEHICLES:")
print(df['VehicleNumber'].nunique())

print("\nTOTAL OPERATORS:")
print(df['OperatorName'].nunique())