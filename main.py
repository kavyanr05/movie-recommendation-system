
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# Load movie dataset
@st.cache_data
def load_movies():
    return pd.read_csv("movies.csv")

movies = load_movies()

# Create movie genre features
@st.cache_resource
def create_features(genres):
    vectorizer = CountVectorizer(
        tokenizer=lambda x: x.split('|'),
        token_pattern=None
    )
    genre_matrix = vectorizer.fit_transform(genres)
    return genre_matrix

genre_matrix = create_features(movies["genres"])

# Website heading
st.title("🎬 Movie Recommendation System")
st.write("Discover movies similar to your favourites!")

st.divider()

# Movie selection
st.subheader("Choose Your Favourite Movie")

selected_movie = st.selectbox(
    "Select a movie:",
    movies["title"].tolist()
)

# Recommendation button
if st.button("✨ Recommend Movies", use_container_width=True):

    movie_index = movies.index[
        movies["title"] == selected_movie
    ][0]

    similarity_scores = cosine_similarity(
        genre_matrix[movie_index],
        genre_matrix
    ).flatten()

    similar_indices = similarity_scores.argsort()[::-1]

    recommendations = [
        i for i in similar_indices if i != movie_index
    ][:5]

    st.subheader("🍿 Your Recommended Movies")

    for number, index in enumerate(recommendations, start=1):
        st.write(f"**{number}. {movies.iloc[index]['title']}**")
        st.caption(f"Genres: {movies.iloc[index]['genres']}")

st.divider()
st.caption("Built with Python, Pandas, Scikit-learn and Streamlit")
