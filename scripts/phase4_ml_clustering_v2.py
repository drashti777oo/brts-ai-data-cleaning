import pandas as pd
from sklearn.cluster import KMeans

print("Loading processed data sample...")

df = pd.read_csv("../output/cleaned_brts.csv", nrows=300000)

print("Extracting unique GPS points...")

coords = df[['Latitude','Longitude']].drop_duplicates()

print("Unique coordinate points:", len(coords))

print("Training KMeans clustering model...")

kmeans = KMeans(
    n_clusters=60,
    random_state=42,
    n_init=10
)

coords['GeoCluster'] = kmeans.fit_predict(coords)

print("Clusters created")

print("Mapping clusters back to dataset...")

df = df.merge(coords, on=['Latitude','Longitude'], how='left')

print("Adding AI movement classification...")

def movement_state(speed):

    if speed == 0:
        return "Stop"

    elif speed < 10:
        return "Slow"

    elif speed < 25:
        return "Normal"

    else:
        return "Fast"

df['MovementState'] = df['Speed'].apply(movement_state)

print("Movement intelligence added")

print("Saving AI enhanced dataset sample...")

df.to_csv("../output/ai_enhanced_sample.csv", index=False)

print("AI Phase complete")