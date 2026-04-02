import pandas as pd

print("Loading AI enhanced data...")

df = pd.read_csv("../output/ai_enhanced_brts.csv")

print("Total rows:",len(df))

# Extract unique GPS points
locations = df[['Latitude','Longitude']].drop_duplicates()

print("Unique GPS points:",len(locations))

# Save unique coordinates
locations.to_csv("../output/unique_locations.csv",index=False)

print("Saved unique locations file")