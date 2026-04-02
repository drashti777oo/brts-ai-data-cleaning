import pandas as pd

print("Loading data...")

df = pd.read_csv("../output/ai_enhanced_brts.csv")

# Round coordinates
df['Lat_round'] = df['Latitude'].round(3)
df['Lon_round'] = df['Longitude'].round(3)

# Unique rounded points
locations = df[['Lat_round','Lon_round']].drop_duplicates()

print("Unique rounded locations:",len(locations))

# Save
locations.to_csv("../output/reduced_locations.csv",index=False)

print("Saved reduced locations")
