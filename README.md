# 🎬 Movie Recommender System

Welcome to the **Movie Recommender System**, a machine learning-based content recommendation app that suggests movies based on your selected preferences. Built with Streamlit, this app offers personalized movie suggestions and provides an easy-to-use interface for an enhanced user experience.

## 🚀 Features

- **Personalized Recommendations**: Select a movie, and the system will suggest five similar movies you might enjoy.
- **Poster Display**: Each recommendation is displayed with a movie poster fetched dynamically from The Movie Database (TMDb).
- **Interactive Interface**: Easy-to-use Streamlit interface with movie selections and instant results.

## 💻 Tech Stack

- **Python**: Core programming language.
- **Streamlit**: For building an interactive web app.
- **Machine Learning**: Uses content-based recommendation.
- **TMDb API**: For fetching movie posters.
- **Pickle**: For loading precomputed movie data and similarity scores.

## 📄 How It Works

1. The app uses a precomputed similarity matrix to find movies similar to the one the user selects.
2. Based on the similarity scores, the app fetches the top five movies most similar to the selected movie.
3. The app then retrieves and displays posters for these movies from TMDb, providing a visually engaging user experience.

## 📂 Project Structure

- `app.py`: Main application script.
- `movie_dict.pkl`: Dictionary of movies and their details.
- `similarity.pkl`: Precomputed similarity matrix for movie recommendations.

## ⚙️ Installation

1. Clone the repository:
   git clone https://github.com/yourusername/movie-recommender-system.git
   cd movie-recommender-system

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app.py

## 🖼️ Screenshots

# 🎬 Movie Recommender System

Welcome to the **Movie Recommender System**, a machine learning-based content recommendation app that suggests movies based on your selected preferences. Built with Streamlit, this app offers personalized movie suggestions and provides an easy-to-use interface for an enhanced user experience.

## 🚀 Features

- **Personalized Recommendations**: Select a movie, and the system will suggest five similar movies you might enjoy.
- **Poster Display**: Each recommendation is displayed with a movie poster fetched dynamically from The Movie Database (TMDb).
- **Interactive Interface**: Easy-to-use Streamlit interface with movie selections and instant results.

## 💻 Tech Stack

- **Python**: Core programming language.
- **Streamlit**: For building an interactive web app.
- **Machine Learning**: Uses content-based recommendation.
- **TMDb API**: For fetching movie posters.
- **Pickle**: For loading precomputed movie data and similarity scores.

## 📄 How It Works

1. The app uses a precomputed similarity matrix to find movies similar to the one the user selects.
2. Based on the similarity scores, the app fetches the top five movies most similar to the selected movie.
3. The app then retrieves and displays posters for these movies from TMDb, providing a visually engaging user experience.

## 📂 Project Structure

- `app.py`: Main application script.
- `movie_dict.pkl`: Dictionary of movies and their details.
- `similarity.pkl`: Precomputed similarity matrix for movie recommendations.

## ⚙️ Installation

1. Clone the repository:
   git clone https://github.com/yourusername/movie-recommender-system.git
   cd movie-recommender-system

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app.py

## 🖼️ Screenshots

![Movie Recommendation Screenshot](path/to/your/screenshot.png)

## 📑 Usage

1. Run the app using `streamlit run app.py`.
2. Select a movie from the dropdown list.
3. Click on the **Recommend** button.
4. View the list of recommended movies along with their posters.

## 🛠️ Dependencies

- `streamlit`
- `requests`
- `pandas`
- `pickle`

Install dependencies by running:
pip install -r requirements.txt

## 🌐 API

This app uses the [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api) to fetch movie posters. You will need an API key from TMDb to use this feature.

## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request with improvements or suggestions.

## 📧 Contact

For questions, please reach out to [your-email@example.com](mailto:your-email@example.com).

---

Enjoy your personalized movie recommendations! 🍿🎉


## 📑 Usage

1. Run the app using
   ```bash
     streamlit run app.py
   ```
3. Select a movie from the dropdown list.
4. Click on the **Recommend** button.
5. View the list of recommended movies along with their posters.

## 🛠️ Dependencies

- `streamlit`
- `requests`
- `pandas`
- `pickle`

Install dependencies by running:
```bash
pip install -r requirements.txt
```

## 🌐 API

This app uses the [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api) to fetch movie posters. You will need an API key from TMDb to use this feature.



Enjoy your personalized movie recommendations! 🍿🎉
