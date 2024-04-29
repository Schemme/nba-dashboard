import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

st.title('6th man of the year votes')
df = pd.read_csv('sixth-man.csv')
#Split player name away from it's team, unimportant
df['Player'] = df['Player'].str.split(',').str[0]

#Make sidebar with votes to display
st.header("Choose votes to Display")
check_1 = st.checkbox("1st Votes", value=False)
check_2 = st.checkbox("2nd Votes", value=False)
check_3 = st.checkbox("3rd Votes", value=False)
# Make the dataframe have desired votes as well as players
columns_to_display = []
colors={}
columns_to_display.append('Player')
if check_1:
    columns_to_display.append('1st votes')
    colors['1st votes'] = '#FFCC00'
if check_2:
    columns_to_display.append('2nd votes')
    colors['2nd votes'] = '#E8E8E8'
if check_3:
    columns_to_display.append('3rd votes')
    colors['3rd votes'] = '#663300'



# Group the data by player and sum the votes for each player
grouped_data = df.groupby('Player')[columns_to_display].sum()
players_order = ['Naz Reid', 'Malik Monk', 'Bobby Portis Jr.',
                 'Norman Powell', 'Bogdan Bogdonavic', 'Jose Alvarado', 'Russel Westbrook',
                 'T.J McConnell', 'Jonathan Isaac', 'Jaime Jaquez Jr.']
grouped_data = grouped_data.reindex(players_order)
grouped_data_without_player = grouped_data.drop(columns=['Player'])

# Create and display the bar chart
if columns_to_display:
    st.subheader("Distribution of votes")
    fig = px.bar(grouped_data_without_player,  color_discrete_map=colors)
    fig.update_layout(plot_bgcolor='#161B21', title='Votes Distribution', xaxis_title='Player', yaxis_title='Votes')
    st.plotly_chart(fig)
else:
    st.warning("Please select at least one column to display")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)
