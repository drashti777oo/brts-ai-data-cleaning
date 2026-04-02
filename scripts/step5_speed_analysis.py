import pandas as pd

print("Loading data...")

df = pd.read_csv("../output/time_fixed_brts.csv")

print("Total rows:",len(df))

# Count speed zero
speed_zero = (df['Speed']==0).sum()

print("Speed = 0 rows:",speed_zero)

# Check speed > 80 (possible anomalies)
fast = (df['Speed']>80).sum()

print("Speed > 80:",fast)

# Vehicle wise average speed
vehicle_speed = df.groupby('VehicleNumber')['Speed'].mean()

print("\nVehicle average speed sample:")
print(vehicle_speed.head())

# Speed distribution
print("\nSpeed summary:")
print(df['Speed'].describe())