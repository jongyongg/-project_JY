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

# 페이지 선택을 위한 multiselect 위젯
page_options = ['선수 정보', '선호하는 발', '인기 있는 국적', '키 분포', '몸무게 분포', '상위 클럽', '상위 포지션']
selected_page = st.multiselect('페이지 선택', page_options)

# 선택된 페이지에 따라 해당하는 그래프를 표시
if '선수 정보' in selected_page:
    st.write("선수 명단 및 정보:")
    sorted_players_info = df_selected.sort_values(by='overall', ascending=False)[['short_name', 'height_cm', 'weight_kg', 'club_name', 'nationality_name', 'overall']]
    st.dataframe(sorted_players_info)

if '선호하는 발' in selected_page:
    players_preferred_foot_labels = df["preferred_foot"].value_counts().index 
    players_preferred_foot_values = df["preferred_foot"].value_counts().values 

    fig, ax = plt.subplots(figsize=(6, 6))
    explode = [0.05, 0.05]
    ax.pie(players_preferred_foot_values, labels=players_preferred_foot_labels, autopct='%.1f%%', startangle=320, counterclock=False, explode=explode, shadow=True)
    ax.set_title('Players Preferred Feet', color='black', fontsize=30)
    st.pyplot(fig)

if '인기 있는 국적' in selected_page:
    top10 = data['nationality_name'].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(top10.index, top10.values)
    ax.set_title('Popular Nationalities')
    st.pyplot(fig)

if '키 분포' in selected_page:
    plt.figure(figsize=(40, 20))
    sns.histplot(data, x="height_cm")
    plt.title("Height Distribution (cm)")
    st.pyplot()

if '몸무게 분포' in selected_page:
    plt.figure(figsize=(40, 20))
    sns.histplot(data, x="weight_kg")
    plt.title("Weight Distribution (kg)")
    st.pyplot()

if '상위 클럽' in selected_page:
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

if '상위 포지션' in selected_page:
    plt.figure(figsize=(40, 24))
    top_player_positions = df_selected['player_positions'].value_counts().head(10)
    sns.barplot(x=top_player_positions.index, y=top_player_positions.values, palette='viridis')
    plt.xticks(rotation=45)
    plt.xlabel('Player Positions')
    plt.ylabel('Count')
    plt.title('Top 10 Player Positions')
    st.pyplot()

