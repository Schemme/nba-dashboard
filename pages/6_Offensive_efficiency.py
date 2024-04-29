import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the data
url = "https://raw.githubusercontent.com/Brevon1104/dsc205/main/team%20stats.csv"
df = pd.read_csv(url)

# Sidebar - Division selection
division_options = df['DIVISION'].unique()
selected_division = st.selectbox('Select Division', division_options)

# Filter data based on selected division
division_df = df[df['DIVISION'] == selected_division]

# Plotting
@st.cache_resource
def plot_stats(data):
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Bar widths
    bar_width = 0.35

    # Adjusting the positions of the bars for each team
    x_positions = range(len(data['TEAM'].unique()))

    # Plotting PPG and oEFF
    for i, team in enumerate(data['TEAM'].unique()):
        team_data = data[data['TEAM'] == team]
        axs[0].bar(x_positions[i], team_data['PPG'].iloc[0], width=bar_width, color='red', label='PPG', alpha=0.7)
        axs[0].bar(x_positions[i] + bar_width, team_data['oEFF'].iloc[0], width=bar_width, color='blue', label='oEFF', alpha=0.7)

    # Custom legend for PPG and oEFF
    axs[0].legend(['PPG', 'oEFF'], loc='upper right')

    # Set x-axis ticks and labels for PPG and oEFF
    axs[0].set_xticks(x_positions)
    axs[0].set_xticklabels(data['TEAM'].unique(), rotation=45, ha='right')

    # Set title and axis labels for PPG and oEFF
    axs[0].set_title(f'Stats for {selected_division} - PPG and oEFF')
    axs[0].set_ylabel('Values')
    axs[0].set_xlabel('Teams')

    # Set y-axis range for PPG and oEFF
    max_value = max(data[['PPG', 'oEFF']].values.max(), 10)  # Minimum y-axis limit is set to 10 for better visualization
    axs[0].set_ylim(0, max_value + 5)  # Adding a buffer for better visualization

    # Plotting WIN%
    axs[1].bar(x_positions, data['WIN%'], color='#000000', alpha=0.7)

    # Set x-axis ticks and labels for WIN%
    axs[1].set_xticks(x_positions)
    axs[1].set_xticklabels(data['TEAM'].unique(), rotation=45, ha='right')

    # Set title and axis labels for WIN%
    axs[1].set_title(f'Stats for {selected_division} - WIN%')
    axs[1].set_ylabel('WIN%')
    axs[1].set_xlabel('Teams')

    plt.tight_layout()
    return fig

if len(division_df) > 0:
    st.title('PPG and oEFF Affect on Winning')
    st.write("""This model allows us to see the correlation between offensive efficiency and points per game for a team and their resulting win percentage. Obviously offense is needed to win games but it's important to see if the teams that are scoring more, and doing so efficiently, are winning more. This also allows us to see which teams are performing the best in their division.""") 
    fig = plot_stats(division_df)
    st.pyplot(fig)

