import streamlit as st
import pandas as pd

@st.cache
def load_data():
    data_path = '2023-2024 NBA Player Stats_exported.csv'
    data = pd.read_csv(data_path)
    return data

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

    # Analyze the closeness of the competition
    max_score = top_defenders['Defensive Score'].iloc[0]
    top_defenders['Score Difference (%)'] = ((max_score - top_defenders['Defensive Score']) / max_score) * 100

    # Narrative description
    st.markdown("""
    ### Analysis of DPOY Contenders
    The table above shows the top three contenders for the NBA Defensive Player of the Year. The 'Defensive Score' is calculated based on key defensive metrics including blocks, steals, and rebounds. The close percentages indicate how tight the competition is this season.
    """)

    # Show some basic stats in a nicer format and add closeness description
    for index, player in top_defenders.iterrows():
        score_diff = player['Score Difference (%)']
        st.subheader(f"{player['Player']} ({player['Tm']})")
        st.text(f"Blocks: {player['BLK']}, Steals: {player['STL']}, Defensive Rebounds: {player['DRB']}, Total Rebounds: {player['TRB']}")
        st.write(f"Score Difference from Top: {score_diff:.2f}%")

if __name__ == "__main__":
    main()
