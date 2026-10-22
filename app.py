
import streamlit as st

st.set_page_config(
    page_title="Fake News Detection System",
    page_icon="📰",
    layout="wide"
)

# Custom CSS
st.markdown(
    """
    <style>

    .stApp {
        background-color: #0B0F19;
        color: white;
    }

    .main-title {
        font-size: 60px;
        font-weight: bold;
        color: white;
        text-align: center;
        margin-top: 30px;
    }

    .subtitle {
        text-align: center;
        color: #9CA3AF;
        font-size: 20px;
        margin-bottom: 40px;
    }

    .feature-card {
        background: linear-gradient(145deg, #111827, #1F2937);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #374151;
        transition: 0.3s;
        margin-bottom: 20px;
    }

    .feature-card:hover {
        transform: scale(1.03);
        border: 1px solid #60A5FA;
        box-shadow: 0px 0px 25px rgba(96,165,250,0.3);
    }

    .feature-title {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 10px;
        color: white;
    }

    .feature-text {
        color: #D1D5DB;
        font-size: 16px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        background: linear-gradient(to right, #2563EB, #1D4ED8);
        color: white;
        font-size: 18px;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background: linear-gradient(to right, #1D4ED8, #1E40AF);
        transform: scale(1.02);
    }

    .sidebar .sidebar-content {
        background-color: #111827;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("📰 Fake News AI")

st.sidebar.info(
    """
    Advanced Fake News Detection System

    Powered by:
    - Machine Learning
    - NLP
    - TF-IDF
    - Logistic Regression
    """
)

st.sidebar.success("System Status: ONLINE")

# Hero Section
st.markdown(
    '<div class="main-title">Fake News Detection Platform</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Real-Time AI Powered News Verification System</div>',
    unsafe_allow_html=True
)

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model Accuracy", "98%")

with col2:
    st.metric("Dataset Size", "44K+")

with col3:
    st.metric("Prediction Speed", "<1 sec")

st.markdown("---")

# Feature Cards
col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">📰 Live News Analysis</div>
            <div class="feature-text">
                Analyze real-time headlines using live APIs and Machine Learning prediction.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.button("Open Live News Analyzer")

with col2:

    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">✍ Manual Prediction</div>
            <div class="feature-text">
                Enter custom news articles and instantly detect fake or real news.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.button("Open Manual Prediction")

st.markdown("---")

# AI Section
st.subheader("⚡ AI Intelligence Engine")

st.write(
    """
    The platform uses Natural Language Processing (NLP) and Machine Learning algorithms
    to analyze textual patterns, semantic structures, and writing behavior in news articles.
    """
)

# Timeline Section
st.subheader("📊 System Workflow")

st.write(
    """
    1. News Collection
    2. Text Preprocessing
    3. TF-IDF Vectorization
    4. Machine Learning Prediction
    5. Real-Time Classification
    """
)

st.markdown("---")

st.success("System Ready for Real-Time Fake News Detection")
