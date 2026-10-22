import pandas as pd
import nltk
import re
import pickle

from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Labels
fake["label"] = 1
true["label"] = 0

# Combine datasets
df = pd.concat([fake, true])

# Shuffle
df = df.sample(frac=1).reset_index(drop=True)

# Keep required columns
df["combined"] = df["title"] + " " + df["text"]

df = df[["combined", "label"]]

df = df.rename(columns={"combined": "text"})

# Download stopwords
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

# Clean text
def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z]', ' ', text)

    words = text.split()

    words = [word for word in words if word not in stop_words]

    return " ".join(words)

df["text"] = df["text"].apply(clean_text)

# Vectorization
vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(df["text"])

y = df["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LogisticRegression()

model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
pickle.dump(model, open("model.pkl", "wb"))

pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved successfully")