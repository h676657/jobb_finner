import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity

#   Laster inn modell og data
@st.cache_resource
def load_model():
    vectorizer=joblib.load("model/tfidf_vectorizer.pkl")
    tfidf_matrix=joblib.load("model/tfidf_matrix.pkl")
    df = pd.read_csv("model/job_data_cleaned.csv")
    return vectorizer, tfidf_matrix, df

vectorizer, tfidf_matrix, df = load_model()

#Web side oppsettet
st.set_page_config(page_title="Jobbfinner", page_icon="fa-suitcase")
st.title("Jobbfinner")
st.write("Skriv inn dine ferdigheter, erfaringer eller interesser, så finner jobbfinnern jobber som passer deg best!")

#Brukerinput!
user_input = st.text_area("Dine ferdigheter / interesser:", placeholder="Python, maskinlæring, ledelse, dataanalyse...")
if st.button("Finn jobber"):
    if len(user_input.strip()) < 3:
        st.warning("Skriv inn minst en ferdighet eller interesse.")
    else:
        # Vektoriserer bruker sin tekst
        user_vector = vectorizer.transform([user_input])

        #Beregner likhet mellom jobber
        similarites = cosine_similarity(user_vector, tfidf_matrix)

        #Finner de 5 mest relevante jobbene
        top_indices = similarites[0].argsort()[-5:][::-1]
        results = df.iloc[top_indices][["job_title", "company", "location", "salary_range", "skills", "job_description"]]

        st.subheader("Topp 5 jobber som matcher deg:")
        for i, row in results.iterrows():
            st.markdown(f"### {row['job_title']} - {row['company']}")
            st.markdown(f"**Sted:** {row['location']} **Lønn:** {row['salary_range']}")
            st.markdown(f"**Ferdigheter:** {row['skills']}")
            st.markdown(f"**Beskrivelse** {row['job_description'][:300]}")
            st.divider()
            