import pandas as pd

print("Loading AI enhanced dataset...")

df = pd.read_csv("../output/ai_enhanced_sample.csv")

print("\nDataset shape:")
print(df.shape)

print("\nNew columns created:")
print(df[['GeoCluster','MovementState']].head())

print("\nCluster distribution:")

print(df['GeoCluster'].value_counts().head(10))

print("\nMovement distribution:")

print(df['MovementState'].value_counts())

print("\nChecking missing values in new columns:")

print(df[['GeoCluster','MovementState']].isnull().sum())

print("\nUnique clusters created:")

print(df['GeoCluster'].nunique())

print("\nValidation complete")