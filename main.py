import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🚀 Streamlit Demo Application")
st.write("This is a simple demo app showcasing Streamlit features.")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Settings")

name = st.sidebar.text_input("Enter your name", "Guest")
age = st.sidebar.slider("Select your age", 10, 80, 25)
show_data = st.sidebar.checkbox("Show Sample Data", True)

# -----------------------------
# Main Content
# -----------------------------
st.subheader("👋 Welcome Section")
st.success(f"Hello **{name}**, you are **{age}** years old!")

# -----------------------------
# Sample Data
# -----------------------------
if show_data:
    st.subheader("📊 Sample Data Table")

    df = pd.DataFrame(
        np.random.randn(10, 3),
        columns=["Column A", "Column B", "Column C"]
    )

    st.dataframe(df, use_container_width=True)

    st.subheader("📈 Line Chart")
    st.line_chart(df)

# -----------------------------
# User Input Example
# -----------------------------
st.subheader("📝 Feedback Form")

feedback = st.text_area("Your feedback")
rating = st.selectbox("Rate this app", [1, 2, 3, 4, 5])

if st.button("Submit"):
    st.toast("Feedback submitted successfully 🎉")
    st.write("⭐ Rating:", rating)
    st.write("💬 Feedback:", feedback)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("© 2026 | Streamlit Demo App")
