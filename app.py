import streamlit as st
import pandas as pd
import pickle
import requests
import os

TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

# ---------- Create folder for pickles ----------
os.makedirs("artificats", exist_ok=True)

# ---------- Download pickles if not present ----------
def download_file(url, save_path):
    if not os.path.exists(save_path):
        with st.spinner(f"Downloading {os.path.basename(save_path)}..."):
            r = requests.get(url, stream=True)
            r.raise_for_status()
            with open(save_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

# Replace these URLs with your Kaggle/Drive direct links
MOVIE_PICKLE_URL = "YOUR_MOVIE_LIST_PICKLE_URL"
SIMILARITY_PICKLE_URL = "YOUR_SIMILARITY_PICKLE_URL"

MOVIE_PICKLE_PATH = os.path.join("artificats", "movie_list.pkl")
SIMILARITY_PICKLE_PATH = os.path.join("artificats", "similarity.pkl")

download_file(MOVIE_PICKLE_URL, MOVIE_PICKLE_PATH)
download_file(SIMILARITY_PICKLE_URL, SIMILARITY_PICKLE_PATH)

# ---------- Load pickle files ----------
try:
    movies = pd.read_pickle(MOVIE_PICKLE_PATH)
    with open(SIMILARITY_PICKLE_PATH, "rb") as f:
        similarity = pickle.load(f)
except Exception as e:
    st.error(f"Error loading pickle files: {e}")
    st.stop()

# ---------- Fetch poster from TMDB ----------
@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
    except:
        pass
    return "https://placehold.co/500x750/333/FFFFFF?text=No+Poster"

# ---------- Recommend movies ----------
@st.cache_data
def recommend(movie_title, movies, similarity):
    try:
        index = movies[movies['title'] == movie_title].index[0]
    except IndexError:
        st.error("Movie not found in dataset.")
        return []

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recs = []

    for i in distances[1:6]:
        movie_data = movies.iloc[i[0]].to_dict()
        movie_data['poster'] = fetch_poster(movie_data['movie_id'])
        recs.append(movie_data)
    return recs

# ---------- Streamlit App ----------
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
