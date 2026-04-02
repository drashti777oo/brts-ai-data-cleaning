import pandas as pd

file1 = "../raw_data/jbm1 16-20.csv"
file2 = "../raw_data/jbm2 16-20.csv"

print("Loading sample data from File 1...")

df1 = pd.read_csv(file1, nrows=50000, low_memory=True)

print("\nLoading sample data from File 2...")

df2 = pd.read_csv(file2, nrows=50000, low_memory=True)

print("\n==============================")
print("PHASE 2 VALIDATION START")
print("==============================")

# TIME CONVERSION
print("\nConverting time columns...")

for df in [df1, df2]:
    df['GPSTime'] = pd.to_datetime(df['GPSTime'], errors='coerce')
    df['InsertTime'] = pd.to_datetime(df['InsertTime'], errors='coerce')
    df['UpdatedTime'] = pd.to_datetime(df['UpdatedTime'], errors='coerce')

print("Time conversion done")

# COORDINATE CHECK
print("\nChecking invalid coordinates...")

invalid_coords1 = df1[
    (df1['Latitude'] > 90) |
    (df1['Latitude'] < -90) |
    (df1['Longitude'] > 180) |
    (df1['Longitude'] < -180)
]

invalid_coords2 = df2[
    (df2['Latitude'] > 90) |
    (df2['Latitude'] < -90) |
    (df2['Longitude'] > 180) |
    (df2['Longitude'] < -180)
]

print("Invalid coordinates File 1:", len(invalid_coords1))
print("Invalid coordinates File 2:", len(invalid_coords2))

# SPEED CHECK
print("\nChecking invalid speeds...")

invalid_speed1 = df1[
    (df1['Speed'] < 0) |
    (df1['Speed'] > 120)
]

invalid_speed2 = df2[
    (df2['Speed'] < 0) |
    (df2['Speed'] > 120)
]

print("Invalid speeds File 1:", len(invalid_speed1))
print("Invalid speeds File 2:", len(invalid_speed2))

# LOCATION CHECK
print("\nChecking Location column...")

print("Missing Location File 1:", df1['Location'].isnull().sum())
print("Missing Location File 2:", df2['Location'].isnull().sum())

# COLUMN COMPARISON
print("\nComparing file structures...")

print("\nFile 1 Columns:")
print(df1.columns)

print("\nFile 2 Columns:")
print(df2.columns)

print("\nDo columns match?")
print(list(df1.columns) == list(df2.columns))

print("\n==============================")
print("PHASE 2 VALIDATION COMPLETE")
print("==============================")


print("\nUnique Location values File 1:")
print(df1['Location'].dropna().unique())

print("\nUnique Location values File 2:")
print(df2['Location'].dropna().unique())