import streamlit as st
import pandas as pd
import matplotlib as plt
import numpy as np
import plotly.express as px

# Read CSV file from GitHub

df=pd.read_csv('Total NBA Stats.csv')

# MVPs list
mvps = ['Nikola Jokić', 'Luka Dončić', 'Shai Gilgeous-Alexander', 'Jayson Tatum', 'Giannis Antetokounmpo', 'Domantas Sabonis','Jalen Brunson','LeBron James','Tyrese Haliburton','Anthony Davis']

# Filter data for MVP candidates
df_mvp = df[df['Player'].isin(mvps)]

# Set  index to 'Player' 
df_mvp.set_index('Player', inplace=True)

# Calculate derived columns
df_mvp['Points per game']= df_mvp['PTS']/df_mvp['G']
df_mvp['Assists per game']= df_mvp['AST']/df_mvp['G']
df_mvp['Rebounds per game']= (df_mvp['ORB']+df_mvp['DRB'])/df_mvp['G']
df_mvp['Blocks per game']= df_mvp['BLK']/df_mvp['G']
df_mvp = df_mvp.round(2)

# Assign ranks to MVPs
rank = [5,7,10,2,3,9,8,1,6,4]
df_mvp['Rank'] = rank

# Select specific columns
df_mvp = df_mvp[['Rank', 'Points per game', 'Assists per game', 'Rebounds per game', 'Blocks per game']]

# Streamlit app
st.header('NBA MVP Comparison')
st.write(df_mvp.sort_values(by='Rank'))
st.markdown("Above is the general consensus between us as to the top 10 players in the NBA right now, just something to guide conclusions a bit.")
# Dropdown menu for selecting player
selected_player = st.selectbox('Select a player:', mvps)

# Dropdown menu for selecting category
selected_category = st.selectbox('Select a category:', ['Points per game', 'Assists per game', 'Rebounds per game', 'Blocks per game'])

# Getting desired specific players specific stat
player_value = df_mvp.loc[selected_player, selected_category]
col_total=df_mvp[selected_category].sum()
PERCENT=(player_value/col_total)*100
PERCENT=PERCENT.round(2)
OPP_PERCENT=100-PERCENT

st.write('The below chart will compare the desired stat of your selected player out and express it as a percentage of all candidates scores. An above average stat (>12 percent of a column) will be displayed in green, an average stat (between 12 and 8%) will be displayed in yellow, and a below average stat (lower than 8%) will be displayed in red. This will allow us to see the stength and weaknesses in a players game, and therefore how good of a player they are overall')

#Values going into chart and conditionals associated with
sizes = [PERCENT, OPP_PERCENT]  
if PERCENT>12:
    col = '#01DF99'
if PERCENT<8:
    col = '#6D0606'
if 8<PERCENT<12:
    col = '#FED406'

# Create DataFrame for plotly pie chart
df_pie=pd.DataFrame({'Player': [selected_player, 'Other Players'], 'Percentage':[PERCENT, OPP_PERCENT]})

# Set colors
colors=['#010129', col]

# Create pie chart using Plotly
fig=px.pie(df_pie, values='Percentage', names='Player', color_discrete_sequence=colors, title=f"{selected_player}'s {selected_category} distribution")
st.plotly_chart(fig, use_container_width=True)

st.header(selected_player)
if selected_player=='Nikola Jokić':
    st.markdown("Nikola Jokić was a frontrunner for MVP last year, to the point of people being upset when he didnt win last year. This year however it was more of the same from the big man, leading his nuggets to the second seed before the playoffs. He has reinvented the position of center in the league, and matches up well with anyone who has to defend him. His consistency, adaptive plystyle, and insane basketball IQ make him the current frontrunner for MVP.")
if selected_player=='Luka Dončić':
    st.markdown("Luka Dončić was a frontrunner for the MVP last year as well, and has put up some absolutely ridiculous numbers this year, averaging almost a triple double a game. However many analysts have taken note of his poor defensive effort, as well as the overall mediocrity of his team is enough to drop him down to the number 2 spot.")
if selected_player=='Shai Gilgeous-Alexander':
    st.markdown("Shai Gilgeous Alexander has been on an absolute tear this season, captaining one of the youngest teams ever in the OKC thunder to the 1 seed. Consistency is the name of Shais game, dropping countless 30 point performances, earning himself the nickname Mr. Consistency. His deep bag and all around play puts him as the 3rd spot for MVP rankings.")
if selected_player=='Jayson Tatum':
    st.markdown("Jayson Tatum is the rock on which the Boston Celtics relied on to dominate the east for another year. Having one of the highest points per game in the league, his consistent offensive output is enough to dominate games. His main weakness is his play in the clutch, and has had his fair share of bad games this year, which knocks him down to 4th for MVP rankings.")
if selected_player=='Giannis Antetokounmpo':
    st.markdown("Giannis Antentokounmpo is one of the only players you could argue had a worse season now than last year. However this by no means he had a bad season this year, using his physical play to dominate in the paint. Leaving a bit to be desired in some aspects, has still had himself a solid year earning a 5th place in the MVP ranking.")
if selected_player=='Domantas Sabonis':
    st.markdown("Domantas Sabonis has established himself as one of the best defensive players in the league, as well as providing consistent offense to a low scoring, defensive kings team. He exemplifies their style of play which has worked for them, earning himself the 6th place in the MVP rankings.")
if selected_player=='Jalen Brunson':
    st.markdown("Jalen Brunson has breathed life into an otherwise pretty mediocre knicks roster to put it simply. His consistent offense mixed with good teamplay has landed him at the 7th place in these MVP rankings.")
if selected_player=='LeBron James':
    st.markdown("An argument can be made for this man being the G.O.A.T of basketball, and his performance this year at the age of 38 has been nothing short of ridiculous. His IQ mixed with his physical prowess make him an incredibly hard player to match up with. However younger players have overtaken the league, and at times he struggles to keep up. This makes him number 8th on these MVP rankings.")
if selected_player=='Tyrese Haliburton':
    st.markdown("Tyrese Haliburton has been a lights-out shooter for the Indiana pacers, placing second in the In-Season tournament with some absolutely ridiculous numbers in it. This mixed with his playmaking makes him a force to be reckoned with. However his game is somewhat one-dimensional, knocking him all the way down to the 9th place in these rankings.")
if selected_player=='Anthony Davis':
    st.markdown("Consistently providing throughout the year for his team, having himself his fair share of ridiculous games. However being on the same team as LeBron, it's easy to get overlooked, and harder to make a case for a real MVP title for him. However that doesn't take away from the season he's had as a two way player who puts up very high minutes on a nightly basis. This earns him the 10th place in these MVP rankings.")
                


