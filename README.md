# News-credibility-software
An AI-powered Fake News Detection System built with Streamlit and Python using TF-IDF vectorization and Logistic Regression.
# 📰 Real-Time Fake News Detection System

An interactive web-based application built with **Streamlit** and **Machine Learning** designed to classify news articles as either **Real** or **Fake** in real-time. 

---

## 🚀 Features
* **Live News Analysis:** Analyze text patterns using NLP and machine learning predictions[cite: 1].
* **Manual Prediction:** Input custom news text/headlines to instantly test authenticity[cite: 1].
* **Interactive UI:** Built with a custom dark-themed Streamlit dashboard.
* **High Performance:** Fast inference time (< 1 sec) powered by a optimized Scikit-Learn pipeline[cite: 1].

---

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Python web framework)
* **Machine Learning:** Scikit-Learn (`LogisticRegression`, `TfidfVectorizer`)
* **Text Preprocessing:** NLTK (Stopwords removal, regex cleaning)
* **Data Manipulation:** Pandas, NumPy

---

## 📊 System Workflow
1. **Data Collection:** Aggregated from benchmark true and false news datasets[cite: 2].
2. **Text Preprocessing:** Lowercasing, punctuation removal, and stopword filtration using NLTK[cite: 2, 3].
3. **Feature Extraction:** Converting text data into numerical vectors using **TF-IDF Vectorizer**[cite: 2].
4. **Model Training:** Training a **Logistic Regression** classifier for binary classification[cite: 2, 3].
5. **Deployment:** Real-time evaluation via a Streamlit web interface[cite: 1, 2].

---

 ## 📂 Dataset
Due to GitHub's file size limits, the training datasets are hosted externally:
* [Download Fake & Real News CSVs (Google Drive)](https://drive.google.com/drive/folders/1Wcxb6pdSOhIEDXybbpNow0f2P4ZqGpac?usp=drive_link)
If you want to re-train the model locally:
1. Download the datasets from the link above (it's a link shared of the fake and real datasets used).
2. Place `Fake.csv` and `True.csv` in the root directory.
3. Run `main.py` to regenerate the trained model (`model.pkl`) and vectorizer (`vectorizer.pkl`)[cite: 3].

---


1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nithinraghavendra/News-credibility-software.git](https://github.com/nithinraghavendra/News-credibility-software.git)
   cd News-credibility-software
  
