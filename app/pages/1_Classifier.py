import streamlit as st
from PIL import Image
import numpy as np
import os
import json
from dotenv import load_dotenv
import dagshub
import mlflow
import tensorflow

st.set_page_config(
    page_title='Classifier',
    layout='wide'
)

# ---------------------------------------------------------------------
# Load Data
# ---------------------------------------------------------------------

with open("../app/data/class_names.json", "r") as f:
    class_names = json.load(f)


# ----------------------------------------------------------------------
# Initialize DagsHub connection and MLflow tracking
# ----------------------------------------------------------------------


dagshub.init(repo_owner='JS-Tharun', repo_name='Garbage-Image-Classifier', mlflow=True)

load_dotenv()

os.environ['MLFLOW_TRACKING_USERNAME'] = f"{os.getenv('MLFLOW_USERNAME')}"
os.environ['MLFLOW_TRACKING_PASSWORD'] = f"{os.getenv('MLFLOW_PASSWORD')}"

mlflow.set_tracking_uri(os.environ['MLFLOW_TRACKING_URI'])
mlflow.set_experiment(os.environ["MLFLOW_EXPERIMENT_NAME"])




# ----------------------------------------------------------------------
# Load the champion models from MLflow and cache it for Streamlit
# ----------------------------------------------------------------------

@st.cache_resource
def load_champion_models():
    prod_models = ['ResNet50_Garbage_Classifier']
    models = []

    for model in prod_models:
        model_uri = f"models:/{model}@champion"
        loaded_model = mlflow.pyfunc.load_model(model_uri)
        models.append(loaded_model)

    return models

with st.spinner("Loading Models..."):
    loaded_models = load_champion_models()




#----------------------------------------------------------------------
# Streamlit App Configuration
#----------------------------------------------------------------------

with st.container():
    st.title("Classify what type of garbage it is")
    with st.form("Garbage Classification Form"):
        image_file = st.file_uploader(
            "Image",
            type=["jpg", "jpeg", "png"]
        )

        submit_button = st.form_submit_button(label="Identify Garbage")

    if submit_button:
        if image_file is not None:
            img = Image.open(image_file)
            img_resized = img.resize((180, 180))
            img_array = np.array(img_resized)
            img_array = np.expand_dims(img_array, axis=0)

            predictions = []

            for model in loaded_models:
                prediction = model.predict(img_array)
                y_pred = np.argmax(prediction, axis=1)[0]
                pred_label = class_names[y_pred]
                predictions.append(pred_label)

            col1, col2 = st.columns(2, border=True)

            with col1:
                st.image(image_file)

            with col2:
                st.write(predictions[0])

        else:
            st.warning("Add an image to classify")