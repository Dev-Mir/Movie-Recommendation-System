import pandas as pd
import streamlit as st
import pickle
import  requests
list_movies = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(list_movies)
def movie_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommendation(movie):
  movie_index = movies[movies['title']==movie].index[0]
  movie_distances = similarmovie[movie_index]
  list_movies = sorted(list(enumerate(movie_distances)),reverse=True,key=lambda x:x[1])[1:6]
  recommended_movies=[]
  recommend_poster=[]
  for i in list_movies:
    movie_id=movies.iloc[i[0]].movie_id
    recommended_movies.append(movies.iloc[i[0]].title)
    recommend_poster.append(movie_poster(movie_id))
  return recommended_movies,recommend_poster

similarmovie = pickle.load(open('similar_movie.pkl','rb'))
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbJ3lmZqjBLZ6HikpkbgJlvlBp887JQJZjKZX-12d4sA&s',width=100)
st.title('Movie Recommendation System')

choose_movie = st.selectbox(
    'Choose a movie for Recommendation',
    movies['title'].values)

if st.button('Recommend Movie'):
    names,posters = recommendation(choose_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
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


