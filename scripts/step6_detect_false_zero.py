import pandas as pd

print("Loading data...")

df = pd.read_csv("../output/time_fixed_brts.csv")

# Sort properly
df = df.sort_values(['VehicleNumber','InsertTime'])

# Previous GPS point
df['prev_lat'] = df.groupby('VehicleNumber')['Latitude'].shift(1)
df['prev_lon'] = df.groupby('VehicleNumber')['Longitude'].shift(1)

# Detect movement
df['moved'] = (
    (df['Latitude'] != df['prev_lat']) |
    (df['Longitude'] != df['prev_lon'])
)

# False zero speed
false_zero = df[(df['Speed']==0) & (df['moved']==True)]

print("False zero speeds:",len(false_zero))

print("Percentage:",
      len(false_zero)/len(df)*100)