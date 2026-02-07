import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("My Android App Streamlit Demo")

# Simple text
st.write("Hello! This Streamlit app can be opened from your Android app.")

# Example interactive slider
x = st.slider("Select a value")
st.write(f"You selected: {x}")

# Example chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
st.line_chart(chart_data)

# Example button
if st.button("Click Me"):
    st.write("Button clicked!")
