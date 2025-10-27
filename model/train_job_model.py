import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

# Leser inn datasettet
df = pd.read_csv("data/job_descriptions.csv")

# Renser kolonnenavn (gjør alt smått og uten mellomrom)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Sjekker hvilke kolonner vi har
print("Kolonner:", df.columns.tolist())

# Fjerner rader som mangler viktig tekst
df = df.dropna(subset=["job_title", "job_description", "skills"])

# Kombiner relevante tekstfelt
df["combined_text"] = (
    df["job_title"].astype(str) + " " +
    df["role"].astype(str) + " " +
    df["skills"].astype(str) + " " +
    df["job_description"].astype(str)
)

# Lager TF-IDF-vektoriserer
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
tfidf_matrix = vectorizer.fit_transform(df["combined_text"])

# Lagrer alt for bruk i Streamlit
os.makedirs("model", exist_ok=True)
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")
joblib.dump(tfidf_matrix, "model/tfidf_matrix.pkl")
df.to_csv("model/job_data_cleaned.csv", index=False)

print("\nModell og data lagret!")
print(f"Antall jobber brukt: {len(df)}")
