import streamlit as st
import pandas as pd
import os

st.title("Battery Analysis Tool")

CSV_PATH = r"C:\Users\beesh\Downloads\research_data.csv"  # <-- your app must create this file

# Start Analysis button (view-side only)
if st.button("Start Analysis"):
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)

        st.success("CSV received. Showing analysis.")

        # Placeholder analysis (safe for demo)
        if "level" in df.columns:
            st.subheader("Battery Levels Over Time")
            st.line_chart(df["level"])
        else:
            st.info("No 'level' column found. Showing raw data.")

        st.subheader("Full Data")
        st.dataframe(df)

        st.download_button(
            "Download CSV",
            df.to_csv(index=False),
            "analysis.csv"
        )
    else:
        st.warning("CSV not found. Please run Start Analysis from main app.")
