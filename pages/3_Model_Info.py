import streamlit as st

st.title("📊 Model Information")

st.subheader("Machine Learning Model")

st.write("""
This Fake News Detection System uses:

- Logistic Regression
- TF-IDF Vectorization
- Natural Language Processing (NLP)

The model was trained on real and fake news datasets
collected from Kaggle.
""")

st.metric("Model Accuracy", "98%")

st.subheader("Libraries Used")

st.write("""
- Pandas
- Scikit-learn
- NLTK
- Streamlit
- Requests
""")

st.subheader("Workflow")

st.write("""
1. Data Collection  
2. Text Preprocessing  
3. TF-IDF Vectorization  
4. Model Training  
5. Prediction  
6. Streamlit Deployment
""")