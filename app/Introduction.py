import streamlit as st

st.set_page_config(
    page_title="Garbage Classifier - Introduction",
    layout="wide"
)

st.title("♻️ Garbage Classification System")

st.markdown("---")

st.header("📌 Problem Statement")
st.write(
    """
    Waste management is a critical global challenge. Improper segregation of garbage 
    leads to inefficient recycling and increased environmental pollution.

    This application aims to solve this problem by using **Deep Learning** to automatically 
    classify waste images into categories such as:
    - Battery
    - Plastic
    - Metal
    - Glass
    - Paper
    - Biological
    - Cardboard
    - Clothes
    - Shoes
    - Trash

    By leveraging image classification techniques, this system helps streamline the 
    recycling process and reduce manual effort in waste sorting.
    """
)

st.markdown("---")

st.header("🚀 Solution Overview")
st.write(
    """
    This app uses a trained deep learning model to analyze images of garbage and predict 
    the type of waste. The goal is to assist in **automating recycling systems** and 
    improving waste segregation efficiency.
    
    """
)

st.markdown("---")

st.header("🧠 How It Works")
st.write(
    """
    1. Upload an image of waste
    2. The image is preprocessed and resized
    3. A trained deep learning model analyzes the image
    4. The system predicts the category of waste
    5. The result is displayed to the user
    """
)

st.markdown("---")

st.header("📂 App Structure")
st.write(
    """
    This application consists of two main pages:

    **1. Introduction**
    - Overview of the project
    - Problem statement and solution

    **2. Garbage Classifier**
    - Upload an image
    - Get prediction results from the model
    """
)

st.markdown("---")

st.success("👉 Navigate to the 'Garbage Classifier' page from the sidebar to start classifying waste!")