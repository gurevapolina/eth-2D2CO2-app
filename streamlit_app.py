import streamlit as st
from time import sleep

st.title("ETH challange - 2D2CO2")

st.subheader("Concept")
st.text("Description of the project - TBA")

uploadedFiles = st.file_uploader(
    label="Upload your PDF file",
    type=['pdf', 'dxf'],
    accept_multiple_files=True,
    label_visibility="hidden"
)

if len(uploadedFiles) != 0:
    with st.spinner("Creating 3D plan..."):
        sleep(10)