import streamlit as st
import pickle
import re

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("✍ Manual News Prediction")

st.write("Enter any news article or headline below.")

# Input
input_text = st.text_area(
    "News Text",
    height=200
)

# Clean text
def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z]', ' ', text)

    return text

# Predict
if st.button("Analyze News"):

    cleaned_text = clean_text(input_text)

    vec = vectorizer.transform([cleaned_text])

    result = model.predict(vec)

    confidence = model.predict_proba(vec)

    st.subheader("Prediction Result")

    if result[0] == 0:
        st.success("✅ REAL NEWS")
    else:
        st.error("❌ FAKE NEWS")

    st.write(
        f"Confidence Score: {max(confidence[0]) * 100:.2f}%"
    )

    st.progress(int(max(confidence[0]) * 100))