import streamlit as st
import pickle
import requests

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Your API Key
API_KEY = "60fb687ecc254c5d9049ad5d9e371830"

# Fetch news
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)

news_data = response.json()

st.title("📰 Live News Analyzer")

if "articles" in news_data:

  for article in news_data["articles"][:15]:

    title = article.get("title", "")

    description = article.get("description", "")

    full_content = article.get("content", "")

    content = title + " " + description + " " + full_content

    source = article["source"]["name"]

    image = article["urlToImage"]

    st.markdown("---")

    if image:
        st.image(image, use_container_width=True)

    st.subheader(title)

    st.caption(f"Source: {source}")

    if st.button(f"Analyze: {title[:20]}"):

        vec = vectorizer.transform([content])

        result = model.predict(vec)
        st.write("Prediction Value:", result[0])

        confidence = model.predict_proba(vec)

        fake_prob = confidence[0][1]
        real_prob = confidence[0][0]

        if real_prob > fake_prob:
            st.success("✅ REAL NEWS")
        else:
            st.error("❌ FAKE NEWS")

        st.write(
            f"Confidence: {max(confidence[0]) * 100:.2f}%"
        )

        st.progress(
            int(max(confidence[0]) * 100)
        )

else:
    st.error("Failed to fetch news.")