🎬 Movies Recommender System

This project is an interactive Movie Recommendation System built with Python and Streamlit. It recommends similar movies based on content similarity and displays their posters using the TMDB API.

⸻

⚙️ Tech Stack • Python 3.9 • Streamlit • Pandas • Scikit-learn • Pickle (for saving model and data) • Requests (for TMDB API)
=======
🎬 Movies Recommender System

This project is an interactive Movie Recommendation System built with Python and Streamlit.
It recommends similar movies based on content similarity and displays their posters using the TMDB API.

⸻

⚙️ Tech Stack
	•	Python 3.9
	•	Streamlit
	•	Pandas
	•	Scikit-learn
	•	Pickle (for saving model and data)
	•	Requests (for TMDB API)
>>>>>>> 5b1daeb07ad35d4926e88d98c52a19f8e97514c1

⸻

📂 Project Structure

<<<<<<< HEAD
. ├── app.py # Main Streamlit application ├── artificats/ # Contains movie_list.pkl & similarity.pkl ├── data/ # Raw TMDB CSV files (tmdb_5000_movies.csv, tmdb_5000_credits.csv) ├── requirements.txt # Python dependencies └── README.md # Project documentation
=======
.
├── app.py                # Main Streamlit application
├── artificats/           # Contains movie_list.pkl & similarity.pkl
├── data/                 # Raw TMDB CSV files (tmdb_5000_movies.csv, tmdb_5000_credits.csv)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

>>>>>>> 5b1daeb07ad35d4926e88d98c52a19f8e97514c1

⸻

🚀 Getting Started

<<<<<<< HEAD
Clone the repository
git clone https://github.com/pranavsoh/Streamlit-app.git cd Streamlit-app

Create & activate a conda environment
conda create -n movies_env python=3.9 -y conda activate movies_env

Install dependencies
pip install -r requirements.txt

Prepare data pickles
The app requires two pickles in the artificats/ folder: • movie_list.pkl → contains preprocessed movie data • similarity.pkl → contains cosine similarity matrix
=======
1. Clone the repository

git clone https://github.com/pranavsoh/Streamlit-app.git
cd Streamlit-app

2. Create & activate a conda environment

conda create -n movies_env python=3.9 -y
conda activate movies_env

3. Install dependencies

pip install -r requirements.txt

4. Prepare data pickles

The app requires two pickles in the artificats/ folder:
	•	movie_list.pkl → contains preprocessed movie data
	•	similarity.pkl → contains cosine similarity matrix
>>>>>>> 5b1daeb07ad35d4926e88d98c52a19f8e97514c1

These pickles can be generated from raw CSV files (tmdb_5000_movies.csv & tmdb_5000_credits.csv) using preprocessing code in app.py.

⸻

<<<<<<< HEAD
Run the app
streamlit run app.py

⸻

📌 Features • Select a movie from the dropdown list. • Get Top 5 recommended movies with posters. • Posters are fetched dynamically using the TMDB API. • Handles missing posters gracefully with a fallback image. • Clean and responsive UI.
=======
5. Run the app

streamlit run app.py


⸻

📌 Features
	•	Select a movie from the dropdown list.
	•	Get Top 5 recommended movies with posters.
	•	Posters are fetched dynamically using the TMDB API.
	•	Handles missing posters gracefully with a fallback image.
	•	Clean and responsive UI.
>>>>>>> 5b1daeb07ad35d4926e88d98c52a19f8e97514c1

⸻

🔑 TMDB API

<<<<<<< HEAD
This project uses the TMDB (The Movie Database) API to fetch movie posters. You need a valid API key from TMDB.
=======
This project uses the TMDB (The Movie Database) API to fetch movie posters.
You need a valid API key from TMDB.
>>>>>>> 5b1daeb07ad35d4926e88d98c52a19f8e97514c1

Replace in app.py:

TMDB_API_KEY = "YOUR_TMDB_API_KEY"

<<<<<<< HEAD
⸻

🧠 How it Works 1. Preprocess raw TMDB CSVs → extract genres, keywords, cast, crew, overview. 2. Combine into tags and vectorize with CountVectorizer. 3. Compute cosine similarity between movies. 4. Store processed data & similarity matrix as pickles. 5. App loads pickles → recommends top 5 similar movies → fetches posters from TMDB API.

⸻

📌 Future Improvements • Deploy on Streamlit Cloud / Hugging Face Spaces. • Add search bar with autocomplete. • Show movie ratings, overview, genres along with posters. • Expand to include collaborative filtering models.
=======

⸻

🧠 How it Works
	1.	Preprocess raw TMDB CSVs → extract genres, keywords, cast, crew, overview.
	2.	Combine into tags and vectorize with CountVectorizer.
	3.	Compute cosine similarity between movies.
	4.	Store processed data & similarity matrix as pickles.
	5.	App loads pickles → recommends top 5 similar movies → fetches posters from TMDB API.

⸻

📌 Future Improvements
	•	Deploy on Streamlit Cloud / Hugging Face Spaces.
	•	Add search bar with autocomplete.
	•	Show movie ratings, overview, genres along with posters.
	•	Expand to include collaborative filtering models.
>>>>>>> 5b1daeb07ad35d4926e88d98c52a19f8e97514c1

⸻

🙌 Author

<<<<<<< HEAD
Pranav Sohaney  GitHub

⸻"# -Movies-Recommender-System" 
=======
Pranav Sohaney
🔗 GitHub

⸻

>>>>>>> 5b1daeb07ad35d4926e88d98c52a19f8e97514c1
