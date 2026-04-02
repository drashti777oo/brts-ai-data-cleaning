import pandas as pd

df = pd.read_csv("../output/final_brts_ai_dataset.csv")

sample = df.sample(1000)

sample.to_csv("../sample_data/sample_brts_data.csv",index=False)

print("Sample dataset created")