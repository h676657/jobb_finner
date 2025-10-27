import pandas as pd
# Leser inn det rensede datasettet
df = pd.read_csv("model/job_data_cleaned.csv")

# Kag et mindre utvalg, vi prøver 10 000
df_subset = df.sample(n=10000, random_state=42)

# Lagrer
df_subset.to_csv("model/job_data_subset.csv", index=False)

print("Lagret subset med 10 000 jobber.")