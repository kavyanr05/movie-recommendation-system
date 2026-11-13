# 🎬 Movie Recommendation System

## Project Overview
This project is a content-based Movie Recommendation System developed using Python and Machine Learning. It recommends movies based on genre similarity.

## Features
- Browse a dataset of 9,742 movies.
- Select a favourite movie from a dropdown menu.
- Get five similar movie recommendations.
- Interactive web application built using Streamlit.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- CountVectorizer
- Cosine Similarity
- Streamlit
- Google Colab

## Dataset
The project uses the MovieLens Latest Small dataset provided by GroupLens Research.

Dataset: https://grouplens.org/datasets/movielens/latest/

## How to Run the Project

1. Clone or download this repository.
2. Install the required libraries:

   `pip install -r requirements.txt`

3. Run the application:

   `streamlit run main.py`

4. Select a movie and click **Recommend Movies**.

## Project Structure

- `main.py` – Streamlit web application
- `movies.csv` – Movie dataset
- `requirements.txt` – Required Python libraries
- `Movie_Recommendation_System.ipynb` – Google Colab notebook

## Recommendation Method
The system uses CountVectorizer to convert movie genres into numerical features and Cosine Similarity to identify movies with similar genres.

## Developed For
Codec Technologies Internship – Project 2
