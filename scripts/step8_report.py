import pandas as pd

raw = pd.read_csv("../output/time_fixed_brts.csv")

ai = pd.read_csv("../output/ai_enhanced_brts.csv")

print("DATA QUALITY REPORT")

print("\nTotal rows:",len(raw))

print("\nSpeed missing BEFORE:",
raw['Speed'].isnull().sum())

print("Speed missing AFTER:",
ai['Speed'].isnull().sum())

print("\nZero speeds before:",
(raw['Speed']==0).sum())

print("Zero speeds after:",
(ai['Speed']==0).sum())

print("\nAverage speed before:",
raw['Speed'].mean())

print("Average speed after:",
ai['Speed'].mean())