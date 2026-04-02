import pandas as pd

print("Loading data...")

df = pd.read_csv("../output/time_fixed_brts.csv")

# Sort properly
df = df.sort_values(['VehicleNumber','InsertTime'])

# Previous GPS
df['prev_lat'] = df.groupby('VehicleNumber')['Latitude'].shift(1)
df['prev_lon'] = df.groupby('VehicleNumber')['Longitude'].shift(1)

# Detect movement
df['moved'] = (
    (df['Latitude'] != df['prev_lat']) |
    (df['Longitude'] != df['prev_lon'])
)

# Convert false zero to missing
df.loc[(df['Speed']==0) & (df['moved']==True),'Speed'] = None

print("Missing speed after marking:",
df['Speed'].isnull().sum())

# Vehicle wise interpolation
df['Speed'] = df.groupby('VehicleNumber')['Speed'].transform(
    lambda x: x.interpolate()
)

# Fill remaining with vehicle mean
df['Speed'] = df.groupby('VehicleNumber')['Speed'].transform(
    lambda x: x.fillna(x.mean())
)

# Final safety fill
df['Speed'] = df['Speed'].fillna(df['Speed'].mean())

print("Missing after imputation:",
df['Speed'].isnull().sum())

# Cleanup helper columns
df = df.drop(columns=['prev_lat','prev_lon','moved'])

# Save AI enhanced data
df.to_csv("../output/ai_enhanced_brts.csv",index=False)

print("AI speed imputation complete")