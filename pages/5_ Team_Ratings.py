import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

def load_data():
    # Load the data from a CSV file
    csv_file_path = '2023-2024 NBA Player Stats_exported.csv'
    df = pd.read_csv(csv_file_path)
    # Calculate ratings
    df['Offensive_Rating'] = df['PTS']  # Assume PTS is the offensive rating
    df['Defensive_Rating'] = df['STL'] + df['BLK']  # Sum of steals and blocks as the defensive rating
    return df

def calculate_team_ratings(df):
    # Group by team and calculate mean ratings
    return df.groupby('Tm').agg({
        'Offensive_Rating': 'mean', 
        'Defensive_Rating': 'mean'
    }).reset_index()

def plot_bar_chart(data, selected_teams, rating_type):
    # Filter data for selected teams
    filtered_data = data[data['Tm'].isin(selected_teams)]
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    team_indices = range(len(filtered_data))  # Team indices
    color = 'blue' if rating_type == 'Defensive_Rating' else 'red'
    ax.bar(team_indices, filtered_data[rating_type], color=color, label=rating_type)

    ax.set_xlabel('Teams')
    ax.set_ylabel('Rating')
    ax.set_title(f'Team {rating_type}')
    ax.set_xticks(team_indices)
    ax.set_xticklabels(filtered_data['Tm'])
    ax.legend()

    st.pyplot(fig)

def plot_scatter_plot(data, selected_teams):
    filtered_data = data[data['Tm'].isin(selected_teams)]
    fig = px.scatter(filtered_data, x='Defensive_Rating', y='Offensive_Rating', color='Tm', 
                     hover_data=['Tm'], title='Offensive vs Defensive Ratings')
    st.plotly_chart(fig)

def main():
    st.title("NBA Team Ratings Visualization")
    st.write("""
    NBA Team Ratings Visualization app. This tool allows you to compare the offensive and defensive ratings of NBA teams for the 2023-2024 season.
    """)
    
    st.markdown("""
    ### Ratings Explanation
    - **Offensive Rating**: This rating is calculated based on the total points scored (PTS) by the players. A higher offensive rating indicates a better offensive performance.
    - **Defensive Rating**: This rating is the sum of steals (STL) and blocks (BLK) by the players, representing the team's defensive capabilities. Higher values suggest stronger defense.
    """)
    
    df = load_data()
    team_ratings = calculate_team_ratings(df)

    # Dropdown to select teams
    teams = team_ratings['Tm'].unique().tolist()
    selected_teams = st.multiselect('Select teams to compare:', teams, default=[])

    # Checkbox to select rating type
    st.write("Select rating types:")
    show_offensive_rating = st.checkbox('Offensive Rating')
    show_defensive_rating = st.checkbox('Defensive Rating')

    if show_offensive_rating and not show_defensive_rating:
        plot_bar_chart(team_ratings, selected_teams, 'Offensive_Rating')
    elif not show_offensive_rating and show_defensive_rating:
        plot_bar_chart(team_ratings, selected_teams, 'Defensive_Rating')
    elif show_offensive_rating and show_defensive_rating:
        plot_scatter_plot(team_ratings, selected_teams)
    else:
        st.write("Select at least one rating type to display.")

if __name__ == "__main__":
    main()
