import requests
import streamlit as st
import pickle
import pandas as pd

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6b10226f65eae07e520b793995c983f6&language=en-US'.format(movie_id))
    data = response.json()
    
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recomend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recomende_movies = []
    recomendes_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        recomende_movies.append(movies.iloc[i[0]].title)
        #fetch poster from api
        recomendes_movies_poster.append(fetch_poster(movie_id))
    return recomende_movies, recomendes_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict )
similarity = pickle.load(open('similartiy.pkl', 'rb'))

st.title('Movie Recomenor System')
selected_movie_name = st.selectbox(
    'Are you bored, Cheakout These !!!',
    (movies['title'].values)
)

if st.button('Recomend'):
    names,posters = recomend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
