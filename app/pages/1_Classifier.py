import streamlit as st

st.set_page_config(
    page_title='Classifier',
    layout='wide'
)

with st.container():
    st.title("Classify what type of garbage it is")
    image_file = st.file_uploader(
        "Image",
        type=["jpg", "jpeg", "png"]
    )
    if image_file is not None:
        st.image(image_file)