import pandas as pd
from sklearn.cluster import KMeans

print("Loading processed data...")

df = pd.read_csv("../output/cleaned_brts.csv", nrows=200000)

print("Preparing coordinate data...")

coords = df[['Latitude','Longitude']]

print("Training KMeans model...")

kmeans = KMeans(n_clusters=50, random_state=42)

df['GeoCluster'] = kmeans.fit_predict(coords)

print("Clusters created")

df.to_csv("../output/ai_sample_output.csv", index=False)

print("AI clustering complete")