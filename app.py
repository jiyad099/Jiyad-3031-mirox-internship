import streamlit as st
from PIL import Image

from modules import noise_attack
from modules import stego_attack
from modules import vision_defense
from modules import vision_trgt


st.set_page_config(
    page_title="Vision Attack Simulator",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Vision Attack Simulator")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    st.sidebar.header("Attack Settings")

    attack_type = st.sidebar.selectbox(
        "Attack Type",
        [
            "Gaussian Noise",
            "Pixel Shift"
        ]
    )

    noise_level = st.sidebar.slider(
        "Noise Intensity",
        min_value=0,
        max_value=50,
        value=10
    )

    enable_defense = st.sidebar.checkbox(
        "Enable Defense Filter",
        value=False
    )

    processed = image.copy()

    if attack_type == "Gaussian Noise":

        processed = noise_attack.apply_Gaussian(
            processed,
            noise_level
        )

    elif attack_type == "Pixel Shift":

        processed = noise_attack.apply_pixel_shift(
            processed,
            noise_level
        )

    if enable_defense:

        processed = vision_defense.run_defense_pipeline(
            processed
        )

    prediction = vision_trgt.classify_image(processed)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Processed")
        st.image(processed, use_container_width=True)

    st.markdown("---")

    st.subheader("Target AI Prediction")

    st.success(prediction)

