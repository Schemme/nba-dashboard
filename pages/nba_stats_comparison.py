import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    projections = pd.read_csv('pages/Player Projects Search 2023-24 Preseason - Copy of AVERAGE PROJECTIONS.csv')
    actuals = pd.read_csv('pages/2023-2024 NBA Player Stats_exported.csv')
    return projections, actuals

df_projections, df_stats = load_data()

# Adjust column names in actuals to match projections for consistent comparison
df_stats.rename(columns={'MP': 'MPG', 'FG%': 'FGP', 'FT%': 'FTP', '3P': '3PM', 'PTS': 'PTS'}, inplace=True)

def preprocess_data(df, columns):
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).replace('%', '').replace(',', '.'), errors='coerce')
    return df

# Define the common columns to compare based on projections
common_columns = ['GP', 'MPG', 'FGP', 'FTP', 'PTS', '3PM', 'REB', 'AST', 'STL', 'BLK', 'TO', 'FGM', 'FGA', 'FTM', 'FTA']

df_projections = preprocess_data(df_projections, common_columns)
df_stats = preprocess_data(df_stats, common_columns)

st.title('NBA Player Stats Comparison: 2023-2024 Projections vs. Actuals')

player_list = df_projections['PLAYER'].unique()
selected_player = st.selectbox('Select a Player', player_list)

def plot_player_data(player):
    player_projections = df_projections[df_projections['PLAYER'].str.contains(player, na=False)]
    player_actuals = df_stats[df_stats['Player'].str.contains(player, na=False)]

    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    if not player_projections.empty and not player_actuals.empty:
        categories = common_columns
        x = range(len(categories))
        ax.bar(x, player_projections[categories].values[0], width=0.4, label='Projections', align='center')
        ax.bar(x, player_actuals[categories].values[0], width=0.4, label='Actuals', align='edge')
        ax.set_xticks(x)
        ax.set_xticklabels(categories, rotation=45)
        ax.set_ylabel('Stats')
        ax.legend()
        st.pyplot(fig)
    else:
        st.write("No data available for this player.")

plot_player_data(selected_player)

