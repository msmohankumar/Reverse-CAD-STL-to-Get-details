import os
import streamlit as st

from core.mesh_loader import load_mesh
from core.geometry_analyzer import analyze_geometry
from core.feature_detector import detect_features
from core.nx_journal_generator import generate_nx_journal

from ui.upload_page import upload_stl
from ui.viewer_page import show_mesh
from ui.report_page import show_report

st.set_page_config(
    page_title="Reverse CAD AI",
    layout="wide"
)

st.title("Reverse CAD AI")

uploaded_file = upload_stl()

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    mesh = load_mesh(file_path)

    col1, col2 = st.columns([2,1])

    with col1:

        st.subheader("3D Viewer")

        fig = show_mesh(mesh)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.subheader("Geometry")

        stats = analyze_geometry(mesh)

        show_report(stats)

        st.subheader("Feature Detection")

        features = detect_features(mesh)

        st.json(features)

    nx_code = generate_nx_journal(stats)

    st.download_button(
        "Download NX Journal",
        nx_code,
        file_name="reverse_cad_journal.py"
    )