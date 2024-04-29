import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    data_path = '2023-2024 NBA Player Stats_exported.csv'
    data = pd.read_csv(data_path)
    return data

def plot_histogram(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data['Defensive Score'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Defensive Scores Across NBA Players')
    plt.xlabel('Defensive Score')
    plt.ylabel('Number of Players')
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)

def main():
    st.title('NBA Defensive Player of the Year (DPOY) Contenders')
    data = load_data()

    df = data.copy()
    
    # Calculate a defensive score as a simple sum of key defensive stats
    df['Defensive Score'] = df['BLK'] + df['STL'] + df['DRB'] + 0.5 * df['TRB']
    
    # Get top 3 DPOY contenders based on defensive score
    top_defenders = df.sort_values('Defensive Score', ascending=False).head(3)
    st.write("Top 3 DPOY Contenders based on Defensive Statistics:")
    st.dataframe(top_defenders[['Player', 'Tm', 'BLK', 'STL', 'DRB', 'TRB', 'Defensive Score']])

    # Plotting the histogram of all players' defensive scores
    plot_histogram(df)

    # Narrative and other analyses could go here...
    # For example, analyzing score differences as in your original setup:
    max_score = top_defenders['Defensive Score'].iloc[0]
    top_defenders['Score Difference (%)'] = ((max_score - top_defenders['Defensive Score']) / max_score) * 100
    
    for index, player in top_defenders.iterrows():
        score_diff = player['Score Difference (%)']
        st.subheader(f"{player['Player']} ({player['Tm']})")
        st.text(f"Blocks: {player['BLK']}, Steals: {player['STL']}, Defensive Rebounds: {player['DRB']}, Total Rebounds: {player['TRB']}")
        st.write(f"Score Difference from Top: {score_diff:.2f}%")

if __name__ == "__main__":
    main()
