import streamlit as st
from PIL import Image
import requests


# HuggingFace inference query method
def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

# API and token (to be moved to secrets.toml)
API_URL = "https://api-inference.huggingface.co/models/petroglyphs-nlp-consulting/GeoImages57kB7"
headers = {"Authorization": st.secrets["api_token"]}


# Streamlit interface

logo = Image.open("./logo.png")
st.sidebar.image(logo)

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
    image = Image.open(uploaded_file)
    image.save("./temp.jpg")
    st.image(image, width=200)
    disabled=False

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
        st.image(im_rotate, width=200)
        image = im_rotate
        image.save("./temp.jpg")

st.subheader("Image Labeling")

label = st.button("Label the image...")

if label:
    output = query("./temp.jpg")
    st.write(output)
