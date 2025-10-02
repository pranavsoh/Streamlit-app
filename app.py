import streamlit as st
import pandas as pd
import pickle
import gzip
import os
import requests

# ----------------- Config -----------------
TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
ARTIFACTS_FOLDER = "artificats"

MOVIE_PICKLE_PATH = os.path.join(ARTIFACTS_FOLDER, "movie_list.pkl.gz")
SIMILARITY_PICKLE_PATH = os.path.join(ARTIFACTS_FOLDER, "similarity.pkl.gz")

os.makedirs(ARTIFACTS_FOLDER, exist_ok=True)

# ----------------- Load data -----------------
def load_pickle(path):
    if not os.path.exists(path):
        st.error(f"File not found: {path}")
        st.stop()
    try:
        if path.endswith(".gz"):
            with gzip.open(path, "rb") as f:
                return pickle.load(f)
        else:
            with open(path, "rb") as f:
                return pickle.load(f)
    except Exception as e:
        st.error(f"Error loading {path}: {e}")
        st.stop()

movies = load_pickle(MOVIE_PICKLE_PATH)
similarity = load_pickle(SIMILARITY_PICKLE_PATH)

# ----------------- Fetch poster -----------------
@st.cache_data
def fetch_poster(movie_id):
    if pd.isna(movie_id):
        return "https://placehold.co/500x750/333/FFFFFF?text=No+Poster"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    try:
        res = requests.get(url)
        data = res.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
    except:
        pass
    return "https://placehold.co/500x750/333/FFFFFF?text=No+Poster"

# ----------------- Recommend movies -----------------
@st.cache_data
def recommend(movie_title, movies, similarity):
    if movie_title not in movies['title'].values:
        st.error("Movie not found in dataset.")
        return []
    index = movies[movies['title'] == movie_title].index[0]
    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)
    
    recs = []
    for i in distances[1:6]:  # top 5 recommendations
        movie_data = movies.iloc[i[0]].to_dict()
        movie_data['poster'] = fetch_poster(movie_data.get('movie_id'))
        recs.append(movie_data)
    return recs

# ----------------- Streamlit App -----------------
st.set_page_config(layout="wide")
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Show Recommendations"):
    with st.spinner("Finding recommendations..."):
        recommendations = recommend(selected_movie, movies, similarity)
    
    if recommendations:
        cols = st.columns(len(recommendations))
        for col, movie in zip(cols, recommendations):
            with col:
                st.image(movie['poster'], use_container_width=True)
                st.subheader(movie['title'])
                st.caption(movie.get('tags', ''))
