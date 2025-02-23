import mimetypes
import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="💿 Data Sweeper", page_icon=":bar_chart:", layout="wide")
st.title("💿 Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization.")

uploaded_files = st.file_uploader("Upload your CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        # File details
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {len(file.getbuffer()) / 1024:.2f} KB")

        # Preview data
        st.write("### Preview of DataFrame")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader(f"Data Cleaning Options for {file.name}")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates removed!")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing values filled!")

        # Column selection
        st.header(f"Select the columns to convert for {file.name}")
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Data Visualization
        st.header(f"Data visualization for {file.name}")
        if st.checkbox(f"Show visualization for {file.name}"):
            numeric_cols = df.select_dtypes(include='number')
            if not numeric_cols.empty:
                st.bar_chart(numeric_cols)
            else:
                st.write("No numeric columns available for visualization.")

        # File Conversion
        st.subheader("💿 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to", ["csv", "excel"], key=file.name)

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "csv":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime = "text/csv"
            elif conversion_type == "excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                filename=file_name,
                mime=mime
            )

            st.success(f"Successfully converted {file.name} to {conversion_type} ✅")
