import streamlit as st

def upload_stl():

    uploaded_file = st.file_uploader(
        "Upload STL File",
        type=["stl"]
    )

    return uploaded_file