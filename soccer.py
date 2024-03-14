import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

data = pd.read_csv('players_22.csv')
data_shape = data.shape
st.write("데이터프레임 크기:", data_shape)

df = data[['short_name','age','height_cm','weight_kg','nationality_name','club_name','overall','potential',
          'value_eur','wage_eur','player_positions','preferred_foot','international_reputation',
          'skill_moves', 'work_rate']]
st.write(df.isnull().sum())

df_selected = df[['short_name', 'age', 'height_cm', 'weight_kg','nationality_name','club_name','overall','player_positions','preferred_foot']]

players_preferred_foot_labels = df["preferred_foot"].value_counts().index 
players_preferred_foot_values = df["preferred_foot"].value_counts().values 

fig, ax = plt.subplots(figsize=(6, 6))
explode = [0.05, 0.05]
ax.pie(players_preferred_foot_values, labels=players_preferred_foot_labels, autopct='%.1f%%', startangle=320, counterclock=False, explode=explode, shadow=True)
ax.set_title('Players Preferred Feet', color='black', fontsize=30)
st.pyplot(fig)


from collections import Counter
top10 = data['nationality_name'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(20, 10))
ax.bar(top10.index, top10.values)
ax.set_title('Popular Nationalities')
st.pyplot(fig)


fig, axes = plt.subplots(1, 2, figsize=(40, 20), sharey=True)

sns.histplot(data, ax=axes[0], x="height_cm")
axes[0].set_title("Height Distribution (cm)")

sns.histplot(data, ax=axes[1], x="weight_kg")
axes[1].set_title("Weight Distribution (kg)")

st.pyplot(fig)


teams_df = df.sort_values(by='overall', ascending=False).head(100) 
teams_counts = teams_df['club_name'].value_counts() 

st.write("상위 100명의 선수들이 속한 팀:")
st.write(teams_counts)

plt.figure(figsize=(40, 20), dpi=100)
sns.countplot(x='club_name', data=teams_df, palette='magma', order=teams_counts.head(10).index)
plt.xticks(rotation=90)
plt.xlabel('Club Name')
plt.ylabel('Count')
plt.title('Top 100 Players by Club', fontsize=30)
st.pyplot()


plt.figure(figsize=(40, 24))
top_player_positions = df_selected['player_positions'].value_counts().head(10)
sns.barplot(x=top_player_positions.index, y=top_player_positions.values, palette='viridis')
plt.xticks(rotation=45)
plt.xlabel('Player Positions')
plt.ylabel('Count')
plt.title('Top 10 Player Positions')
st.pyplot()