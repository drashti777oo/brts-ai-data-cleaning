import pandas as pd

file = "../raw_data/jbm1 16-20.csv"

print("Loading sample data...")

df = pd.read_csv(file, nrows=50000, low_memory=True)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nSpeed Statistics:")
print(df['Speed'].describe())

print("\nLatitude/Longitude Statistics:")
print(df[['Latitude','Longitude']].describe())

print("\nUnique Vehicles:")
print(df['VehicleNumber'].nunique())

print("\nSample GPS Times:")
print(df['GPSTime'].head())