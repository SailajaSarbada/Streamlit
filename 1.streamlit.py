# my_app.py
import streamlit as st
import pandas as pd

st.title("Simple Data Summary Tool")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of the data:", df.head())

    st.write("Data Summary:")
    st.write(df.describe())
