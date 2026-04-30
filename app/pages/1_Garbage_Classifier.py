import streamlit as st
from PIL import Image
import numpy as np
import os
import json
from dotenv import load_dotenv
import dagshub
import mlflow
from mlflow.tracking import MlflowClient

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

username = os.getenv("MLFLOW_USERNAME")
password = os.getenv("MLFLOW_PASSWORD")

mlflow.set_tracking_uri(
    f"https://{username}:{password}@dagshub.com/JS-Tharun/Garbage-Image-Classifier.mlflow"
)
mlflow.set_experiment(os.environ["MLFLOW_EXPERIMENT_NAME"])

client = MlflowClient()


# ----------------------------------------------------------------------
# Load the champion models from MLflow and cache it for Streamlit
# ----------------------------------------------------------------------


@st.cache_resource(ttl=3600)  # Cache for 1 hour
def load_champion_models():
    prod_models = ['ResNet50_Garbage_Classifier']
    models = []
    model_versions = []

    for model in prod_models:
        model_uri = f"models:/{model}@champion"
        loaded_model = mlflow.pyfunc.load_model(model_uri)
        model_version = client.get_model_version_by_alias(name=model, alias="champion").version
        models.append(loaded_model)
        model_versions.append(model_version)
        

    return prod_models, models, model_version

model_names, loaded_models, model_versions = load_champion_models()




#----------------------------------------------------------------------
# Streamlit App Configuration
#----------------------------------------------------------------------

st.title("🗑️ Garbage Image Classifier")
st.markdown("Upload an image to classify the type of garbage.")

with st.container():
    with st.form("Garbage Classification Form"):
        image_file = st.file_uploader(
            "Choose an image file",
            type=["jpg", "jpeg", "png"],
            help="Supported formats: JPG, JPEG, PNG"
        )
        submit_button = st.form_submit_button(label="🔍 Classify Garbage")

if submit_button:
    if image_file is not None:
        with st.container(border=True):
            with st.spinner("Classifying..."):
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

            col1, col2 = st.columns([1, 1], gap="large")

            with col1:
                st.subheader("Uploaded Image")
                st.image(image_file)

            with col2:
                st.subheader("Classification Result")
                st.success(f"Predicted: **{predictions[0]}**")
                st.write("Model used for prediction:")
                st.info(f"{model_names[0]} Version{model_versions[0]}")

    else:
        st.error("Please upload an image to classify.")