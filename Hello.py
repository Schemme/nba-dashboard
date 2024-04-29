import streamlit as st

# Assuming the logo is renamed and correctly formatted as 'nba_logo_2024.png'
nba_logo_path = "nba_logo_2024.png"  # Update this path to your actual image file path
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
