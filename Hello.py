import streamlit as st

# Configuring the page
st.set_page_config(page_title="NBA Dashboard", layout="wide", page_icon="🏀")

# Apply a custom theme via your .streamlit/config.toml or directly in the code
# You can uncomment and adjust the following lines to set a theme programmatically
# st.experimental_set_theme({
#     'primaryColor': '#1d428a',
#     'backgroundColor': '#0e1117',
#     'secondaryBackgroundColor': '#262730',
#     'textColor': '#fafafa',
#     'font': 'sans serif'
# })

# Custom CSS to style the markdown
st.markdown(
    '''
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .info-text {
        font-size:16px;
        color: #f63366;  # Bright color for emphasis
    }
    </style>
    ''', unsafe_allow_html=True
)

st.sidebar.success("Select an app above.")

st.title("NBA Dashboard")

st.markdown("""
    <div class='big-font info-text'>This project was made to synthesize the overwhelming amount of NBA data into meaningful visualizations.</div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class='info-text'>Please refer to the sidebar to the left in order to select a visualization.</div>
    """, unsafe_allow_html=True)

# Adding a footer to credit the creators with enhanced styling
st.markdown("---")
st.markdown("Created by **Max Elliott** and **Brady** with :heart:")

# Example of adding interactive elements
team_select = st.sidebar.selectbox("Choose a team to display stats:", ["Lakers", "Warriors", "Celtics", "Bulls"])
if team_select:
    st.write(f"You selected the {team_select}, here are the stats...")

# Placeholder for dynamic data visualization
# This could be a place to add charts or data tables based on the team selection
st.write("Chart or data table will go here based on the team selected.")


