import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
# Model trener for mindre datasett, som kan lastes opp til github
# LESER INN SUBSET (mindre datasett)
df = pd.read_csv("model/job_data_subset.csv")

#Kombiner tekst
df["combined_text"] = (
    df["job_title"].astype(str) + " " +
    df["role"].astype(str) + " " +
    df["skills"].astype(str) + " " +
    df["job_description"].astype(str)
)
# lager ny og mindre TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", max_features=3000)
tfid_matrix = vectorizer.fit_transform(df["combined_text"])

# lagrer filene

joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")
joblib.dump(tfid_matrix, "model/tfidf_matrix.pkl")

print(f" Ny mdodell trent på {len(df)} jobber.")
