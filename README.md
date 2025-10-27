# Jobbfinner

En maskinlæringsbasert webapp som hjelper brukere å finne relevante jobber basert på ferdigheter, interesser og erfaring.  
Prosjektet ble utviklet som en del av **DAT158 – Maskinlæring** ved Høgskolen på vestlandet (HVL).

---

## Demo
Appen er tilgjengelig gratis på **Streamlit Cloud**:  
-> [https://jobb-finner.streamlit.app](https://jobbfinner-l57wogze92anzqmx2jhvqm.streamlit.app/)  

---

## Om prosjektet

**Jobbfinner** bruker en TF-IDF-modell til å analysere jobbannonser og sammenligne dem med brukerens ferdigheter.  
Basert på *cosine similarity* finner modellen de fem mest relevante stillingene.

Prosjektet demonstrerer hvordan tekstbasert maskinlæring kan brukes til å lage et **personlig jobbanbefalingssystem**.

---

## Teknologi

| Komponent | Beskrivelse |
|------------|--------------|
| **Python 3.13** | Programmeringsspråk |
| **Scikit-learn** | TF-IDF og cosine similarity |
| **Pandas** | Databehandling |
| **Streamlit** | Webgrensesnitt og deploy |
| **Job Dataset (syntetisk)** | Kaggle-datasett med 1,6M jobber |

---

## Mappestruktur
```bash
jobb_finner/
├── app/
│   └── app.py                 # Streamlit-app
├── model/
│   ├── train_job_model.py     # Full modelltrening
│   ├── train_job_model_subset.py # Lett versjon for skyen
│   ├── tfidf_vectorizer.pkl   # Lagret modell (tekstvektorisering)
│   ├── tfidf_matrix.pkl       # TF-IDF-matrise for matching
│   └── job_data_subset.csv    # Komprimert datasett
├── data/
│   └── jobs.csv               # Originalt datasett (ikke pushet)
├── requirements.txt
└── README.md
```
---

## Kjør lokalt

1. **Installer avhengigheter**
   ```bash
   pip install -r requirements.txt
2. **Start Appen**
  python -m streamlit run app/app.py
3. **Åpne i nettelser**
   htttps:://localhost:8501


## Kilder
Kaggle: Rana, Ravender S. Job dataset (Syntethic, 2024) https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset



