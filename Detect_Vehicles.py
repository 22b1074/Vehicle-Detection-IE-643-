import streamlit as st
import torch
from PIL import Image
import gdown
import os

# Google Drive file ID
file_id = "10-irxnQvn4MHWSWOZkFpucWjVoFj0XCa"
weights_path = "best_ie643.pt"

def download_weights_from_gdrive(file_id, filename):
    if not os.path.exists(filename):
        url = f"https://drive.google.com/uc?id={file_id}"
        with st.spinner("Downloading model weights from Google Drive..."):
            gdown.download(url, filename, quiet=False)
        st.success("Download complete!")
    else:
        st.info("Weights already downloaded.")

# Download weights if not present
download_weights_from_gdrive(file_id, weights_path)
# Load YOLOv5 model (change path if weights are in a custom location)
@st.cache_resource
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path)
    model.eval()
    return model

model = load_model()

st.title("YOLOv5 Object Detection")
st.markdown("Upload an image and see object detection results.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)

    with st.spinner("Running detection..."):
        results = model(image)

    # Display results (with bounding boxes)
    results.render()  # updates results.imgs with boxes
    st.image(results.ims[0], caption="Detected Image", use_column_width=True)

    # Optionally display raw prediction data
    st.markdown("### Predictions")
    st.dataframe(results.pandas().xyxy[0])  # shows xmin, ymin, xmax, ymax, confidence, class, name
