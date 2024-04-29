import pandas as pd
import streamlit as st

URL = "https://raw.githubusercontent.com/Schemme/FINAL-PROJECT/main/rookie%20data.txt"
df = pd.read_csv(URL)

df.set_index('Player', inplace=True)

st.title('NBA Rookie of the Year Stats')

st.write("""Going into the 2023 draft, French basketball star was drafted with the 1st overall pick to the San Antonio Spurs. He was projected to be the best incoming player the league has seen since LeBron James was drafted out of high school in 2003. With all of this hype came the predictions that he would easily win Rookie of the Year. This model is to show if his first season lived up to the hype.""")

selected_columns = ['FG%', '3P%', 'PTS', 'TRB', 'AST', 'STL', 'BLK', 'G']
df_selected = df[selected_columns]

# Filter the DataFrame to include only players who played at least 65 games
df_filtered = df_selected[df_selected['G'] >= 65]

st.sidebar.title('Select Stat to Filter By')
statistic = st.sidebar.radio('Choose a Statistic', df_filtered.columns[:-1])  # Exclude 'G'

# Sort the filtered DataFrame by the selected statistic
sorted_df = df_filtered.sort_values(by=statistic, ascending=False)

# Select the top 5 players for the selected statistic
top_5_players = sorted_df.head(5)

st.write('## Rookie of the Year Leaders')

# Display the bar chart for the selected statistic
st.bar_chart(top_5_players[statistic])
