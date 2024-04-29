import pandas as pd
import streamlit as st
import plotly.express as px

# Load the CSV file into a pandas DataFrame
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def calculate_per(row):
    per = (row['PTS'] + row['TRB'] + row['AST'] + row['STL'] + row['BLK'] - row['TOV'] - (row['FGA'] - row['FG']) - (0.5 * (row['FTA'] - row['FT'])) / row['MP']) / row['MP']
    return per

def main():
    st.title('All-NBA Team Candidates by PER')

    # Introductory paragraph
    st.write("""At the end of each year the top 15 players in the NBA get voted to an All-NBA team. There are 3 teams each composed of 2 guards, 2 forwards, and 1 center.
Aside from being named MVP, this is the biggest recognition a player can receive for their performances in a year. With that being said we have created this visualization sorted by position to allow you guys to get a feel for who is at the top of the league in terms of performance and might be named to one of the 3 All-NBA teams when the season concludes.""")

    df = load_data('https://raw.githubusercontent.com/Brevon1104/dsc205/main/Total%20NBA%20Stats.csv')

    # Sidebar for position selection
    position = st.sidebar.selectbox('Select Position', df['Pos'].unique())

    # Filter data for selected position
    position_data = df[(df['Pos'] == position) & (df['G'] >= 65)]

    # Calculate PER for each player
    position_data['PER'] = position_data.apply(calculate_per, axis=1)

    # Sort players by PER
    position_data = position_data.sort_values(by='PER', ascending=False)

    # Select top 10 players
    top_10_players = position_data.head(10)

    # Plot PER by player
    fig = px.bar(top_10_players, x='Player', y='PER',color='Player',title=f'Top 10 Players by PER ({position} Position)')
    fig.update_xaxes(title_text='Player')
    fig.update_yaxes(title_text='Player Efficiency Rating')

    # Rotate x-axis labels for better readability
    fig.update_layout(xaxis_tickangle=-45)

    # Show plot
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
