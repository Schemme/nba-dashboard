import streamlit as st

# Provide an absolute path if relative paths fail
nba_logo_path = "/absolute/path/to/nba-dashboard/nba_logo_2024.png"
st.image(nba_logo_path, caption='NBA Logo 2024', width=300)

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
