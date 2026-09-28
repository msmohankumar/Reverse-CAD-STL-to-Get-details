import pandas as pd
import streamlit as st

def show_report(stats):

    df = pd.DataFrame(
        stats.items(),
        columns=["Parameter","Value"]
    )

    st.dataframe(df)