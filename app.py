import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="🎶 Konkani Ballads to Art", layout="centered")

st.markdown("<h1 style='text-align: center;'>🎶 Konkani Ballads → AI Art 🖼️</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Select a ballad and generate a beautiful image using AI!</h4>", unsafe_allow_html=True)
st.divider()

ballad = st.selectbox("🎵 Choose a Ballad", [
    "Lullaby of the Stars",
    "Fisherman's Prayer",
    "Monsoon Memories"
])

if st.button("✨ Generate Artwork"):
    st.info("Generating image... please wait")
    time.sleep(2)  # Your backend will replace this
    image = Image.open("sample_image.png")  # Placeholder
    st.success("Here is your artwork!")
    st.image(image, caption="AI-Generated Art", use_column_width=True)

st.divider()
