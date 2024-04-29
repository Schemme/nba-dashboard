import streamlit as st

# Load and display an image
nba_logo_path = "nba_logo_2024.png"  # If locally saved, or replace with a URL if hosted online
st.image(nba_logo_path, caption='NBA Logo 2024')

st.write("# NBA Dashboard")

st.sidebar.success("Select an app above.")

st.markdown(
    """
    This project was made in order to take in the overwhelming amount of NBA data and create meaningful visualizations from it.
   
    Please refer to the sidebar to the left in order to select a visualization.
    """
)

# Adding a footer to credit the creators
st.markdown("---")
st.markdown("Created by Max Elliott and Brady")
