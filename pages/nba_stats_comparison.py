import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    projections = pd.read_csv('pages/Player Projects Search 2023-24 Preseason - Copy of AVERAGE PROJECTIONS.csv', skiprows=1)
    actuals = pd.read_csv('pages/2023-2024 NBA Player Stats_exported.csv')
    return projections, actuals

df_projections, df_stats = load_data()

# Print columns for debugging
st.write("Projections Columns:", df_projections.columns)
st.write("Actuals Columns:", df_stats.columns)

# Ensure column names are correct
df_stats.rename(columns={
    'MP': 'MPG', 
    'G': 'GP', 
    '3P': '3PM', 
    'TRB': 'REB', 
    'TOV': 'TO',
    'Player': 'PLAYER'
}, inplace=True)

df_projections.rename(columns={
    'FT%': 'FTP', 
    'FG%': 'FGP'
}, inplace=True)

def preprocess_data(df):
    numeric_columns = ['GP', 'MPG', 'FGP', 'FTP', 'PTS', '3PM', 'REB', 'AST', 'STL', 'BLK', 'TO']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].replace(',', '.', regex=True), errors='coerce')
        else:
            st.error(f"Column {col} not found in DataFrame. Please check the data.")
    return df

df_projections = preprocess_data(df_projections)
df_stats = preprocess_data(df_stats)

st.title('NBA Player Stats Comparison: 2023-2024 Projections vs. Actuals')

player_list = df_projections['PLAYER'].unique()
selected_player = st.selectbox('Select a Player', player_list)

def plot_player_data(player):
    player_projections = df_projections[df_projections['PLAYER'].str.contains(player, na=False)]
    player_actuals = df_stats[df_stats['PLAYER'].str.contains(player, na=False)]

    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    if not player_projections.empty and not player_actuals.empty:
        categories = ['GP', 'MPG', 'FGP', 'FTP', 'PTS', '3PM', 'REB', 'AST', 'STL', 'BLK', 'TO']
        x = range(len(categories))
        ax.bar(x, player_projections[categories].iloc[0], width=0.4, label='Projections', align='center')
        ax.bar(x, player_actuals[categories].iloc[0], width=0.4, label='Actuals', align='edge')
        ax.set_xticks(x)
        ax.set_xticklabels(categories, rotation=45)
        ax.set_ylabel('Stats')
        ax.legend()
        st.pyplot(fig)
    else:
        st.write("No data available for this player.")

plot_player_data(selected_player)
