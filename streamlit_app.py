import streamlit as st
from PIL import Image
import requests
import time
import os


models = {
    "B0": "https://api-inference.huggingface.co/models/petroglyphs-nlp-consulting/GeoImages57kB0",
    "B7": "https://api-inference.huggingface.co/models/petroglyphs-nlp-consulting/GeoImages57kB7"
}

headers = {"Authorization": st.secrets["api_token"]}

# HuggingFace inference query method
def query(filename, model=models["B7"]):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(model, headers=headers, data=data)
    return response.json()

# Streamlit interface

logo = Image.open("./logo.png")
st.sidebar.image(logo)

model = st.sidebar.selectbox("Choose the model", list(models.keys()))

st.title("Geosciences Images Classifier")

st.markdown("""
    The Geosciences Images Classifier has been built on top of the Google EfficientNet platform.
    - You can choose between the B0 (smaller one) and B7 architectures.
    - The output tells you which are the top-5 most probable labels with associated scores.
""")

# control the image edition widgets
disabled = True

st.subheader("Image Uploading")

# image uploader
uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg'])

# display the original image
if uploaded_file:
    if not os.path.exists("./temp.jpg"):
        image = Image.open(uploaded_file)
        image.save("./temp.jpg")
        st.image(image, width=200)
        disabled=False
    else:
        image = Image.open("./temp.jpg")
        st.image(image, width=200)
        disabled=False
else:
    st.error("Please upload an image first...")

st.subheader("Image Edition")

st.markdown("Here, you can rotate the image before labeling it for better results.")

if not disabled:
    col1, col2, col3, col4 = st.columns(4)
    rotation_angle = 0
    with col1:
        c90 = st.button("90 degrees clockwise")
    with col2:
        c180 = st.button("180 degrees clockwise")
    with col3:
        ac90 = st.button("90 degrees counter clockwise")
    with col4:
        ac180 = st.button("180 degrees counter clockwise")
    if c90:
        rotation_angle = -90
    elif c180:
        rotation_angle = -180
    elif ac90:
        rotation_angle = 90
    elif ac180:
        rotation_angle = 180
    
    if rotation_angle !=0 :
        im_rotate = image.rotate(rotation_angle, expand=True)
        im_rotate.save("./temp.jpg")
        st.experimental_rerun()

st.subheader("Image Labeling")

label = st.button("Label the image...")

if label:
    output = query("./temp.jpg")
    if type(output)!=list and 'error' in output.keys():
        st.spinner("The model is loading...")
        time.sleep(20)
        output = query("./temp.jpg")
    else:
        os.remove("./temp.jpg")
        cola, colb = st.columns([3, 7])
        with cola:
            for o in output:
                st.slider(label=o['label'], min_value=0., max_value=1., value=o['score'], disabled=True)
