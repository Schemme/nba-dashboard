import streamlit as st

# Customizing the page configuration
st.set_page_config(page_title="NBA Dashboard", page_icon=":basketball:", layout="wide")

st.title("NBA Dashboard")

st.sidebar.success("Select an app above.")

# Sidebar for user inputs
st.sidebar.header("User Input Features")
option = st.sidebar.selectbox(
    'Which statistic do you want to see?',
    ('Scoring Leaders', 'Assist Leaders', 'Rebound Leaders')
)

st.sidebar.date_input("Select a date range")

# Use markdown with custom CSS for better styling
st.markdown(
    """
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    </style>
    <div class="big-font">
    This project was made to synthesize the overwhelming amount of NBA data into meaningful visualizations.
    <br>
    Please refer to the sidebar to select a visualization.
    </div>
    """,
    unsafe_allow_html=True
)

# Placeholder for dynamic content based on user selection
if option == 'Scoring Leaders':
    st.header("NBA Scoring Leaders")
    # Example of a plot
    st.line_chart(data={'Scores': [25, 30, 27, 35, 40]})
elif option == 'Assist Leaders':
    st.header("NBA Assist Leaders")
    # Example of a plot
    st.bar_chart(data={'Assists': [7, 9, 12, 11, 8]})
else:
    st.header("NBA Rebound Leaders")
    # Example of a plot
    st.area_chart(data={'Rebounds': [10, 14, 7, 12, 15]})

# Dynamic footer
st.markdown("---")
st.markdown("Developed by [Your Name or Organization](URL_to_your_profile_or_site)")
