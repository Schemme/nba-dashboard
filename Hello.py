import streamlit as st

# Configuring the page
st.set_page_config(page_title="NBA Dashboard", layout="wide", page_icon="🏀")

# Custom CSS to style the markdown
st.markdown(
    '''
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .nba-color {
        color: #1d428a;  # Dark blue color; change as needed
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
    </style>
    ''', unsafe_allow_html=True
)

st.sidebar.success("Select an app above.")

col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("## NBA Dashboard", unsafe_allow_html=True)
    st.markdown("""
        <div class='nba-color big-font'>This project was made to synthesize the overwhelming amount of NBA data into meaningful visualizations.</div>
        """, unsafe_allow_html=True)

st.markdown("""
    <div class='big-font'>Please refer to the sidebar to the left in order to select a visualization.</div>
    """, unsafe_allow_html=True)

# Adding a footer to credit the creators
st.markdown("---")
st.markdown("Created by **Max Elliott** and **Brady**")
