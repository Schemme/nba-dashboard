import streamlit as st

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
