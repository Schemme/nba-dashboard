import streamlit as st

# Correct path to the image file, assuming your script is at the root of 'nba-dashboard'
nba_logo_path = "nba_logo_2024.png"

st.image(nba_logo_path, caption='NBA Logo 2024', width=300)  # You can adjust the width as needed

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
