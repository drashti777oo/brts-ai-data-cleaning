import pandas as pd

print("Loading data...")

df1 = pd.read_csv("../raw_data/jbm1 16-20.csv", low_memory=False)
df2 = pd.read_csv("../raw_data/jbm2 16-20.csv", low_memory=False)

# Preserve raw data
df_raw = pd.concat([df1, df2], ignore_index=True)

# Working copy
df = df_raw.copy()

print("Initial shape:", df.shape)

# Drop useless column in working dataset only
df = df.drop(columns=['Location'])

print("After dropping Location:", df.shape)

# Convert time columns
df['InsertTime'] = pd.to_datetime(df['InsertTime'], errors='coerce')
df['GPSTime'] = pd.to_datetime(df['GPSTime'], errors='coerce')
df['UpdatedTime'] = pd.to_datetime(df['UpdatedTime'], errors='coerce')

# Fix unrealistic speed
df.loc[df['Speed'] > 100, 'Speed'] = None

# Sort by vehicle and time
df = df.sort_values(['VehicleNumber','InsertTime'])
df = df.reset_index(drop=True)

print("\nCleaning complete")

print("\nMissing after cleaning:")
print(df.isnull().sum())

# Save cleaned version
df.to_csv("../output/cleaned_brts.csv", index=False)

print("\nSaved cleaned dataset")

