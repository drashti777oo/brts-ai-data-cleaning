import pandas as pd

print("Loading datasets...")

df = pd.read_csv("../output/ai_enhanced_brts.csv")

lookup = pd.read_csv("../output/location_lookup.csv")

# Create rounded coordinates
df['Lat_round'] = df['Latitude'].round(3)
df['Lon_round'] = df['Longitude'].round(3)

print("Merging location data...")

df = df.merge(
    lookup,
    on=['Lat_round','Lon_round'],
    how='left'
)

print("Missing locations:",
df['LocationName'].isnull().sum())

# Drop helper columns
df = df.drop(columns=['Lat_round','Lon_round'])

# Save final dataset
df.to_csv("../output/final_brts_ai_dataset.csv",index=False)

print("Final dataset created")