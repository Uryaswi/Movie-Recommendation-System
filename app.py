import streamlit as st
import pandas as pd
import pickle


df = pd.read_pickle("movie_data.pkl")
with open("cosine_similarity.pkl", "rb") as f:
    cs = pickle.load(f)


def movie_recommendor(movie):

    if movie not in df['title'].values:
        return ["Movie not found. Please try another one."]
    
    movie_index = df[df['title'] == movie].index[0]
    

    distances = cs[movie_index]
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    
    recommended_movies = [df.loc[i[0]].title for i in movies]
    return recommended_movies

st.title("Movie Recommendation System")

movie_name = st.text_input("Enter a movie you like:")

if st.button("Search"):
    recommendations = movie_recommendor(movie_name)
    st.write("You may like to watch:")
    for rec_movie in recommendations:
        st.write(rec_movie)
