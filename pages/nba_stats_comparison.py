import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    # Adjust file paths as necessary
    projections = pd.read_csv('path_to_projections_file.csv')
    actuals = pd.read_csv('path_to_actuals_file.csv')

    # Assuming columns are named correctly after loading
    return projections, actuals

df_projections, df_stats = load_data()

# Check column names directly after loading
st.write("Projections Columns:", df_projections.columns)
st.write("Stats Columns:", df_stats.columns)

def preprocess_data(df, columns):
    # Here columns are the ones common and correctly named in both datasets
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).replace('%', '').replace(',', '.'), errors='coerce')
        else:
            st.write(f"Column {col} not found in DataFrame")
    return df

# Define common columns as per the corrected dataset
common_columns = ['G', 'MPG', 'FG%', 'FT%', 'PTS', '3P', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FGM', 'FGA', 'FTM', 'FTA']
df_projections = preprocess_data(df_projections, common_columns)
df_stats = preprocess_data(df_stats, common_columns)

st.title('NBA Player Stats Comparison: 2023-2024 Projections vs. Actuals')

# Ensure player name columns are named 'PLAYER' in both datasets
player_list = df_projections['PLAYER'].unique()
selected_player = st.selectbox('Select a Player', player_list)

def plot_player_data(player):
    player_projections = df_projections[df_projections['PLAYER'].str.contains(player, na=False)]
    player_actuals = df_stats[df_stats['PLAYER'].str.contains(player, na=False)]

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
