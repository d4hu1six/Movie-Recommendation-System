# Movie-Recommendation-System
A smart Python-based movie recommendation system that suggests similar movies based on genre and plot, with ratings and poster links, even if you mistype the movie name.
This Python project is a content-based movie recommendation system.
It recommends movies similar to a user-input movie based on genres and overview descriptions.

The system also handles typos in user input, shows IMDB ratings, genres, and poster links, and provides a numbered list of top N recommendations.

##Libraries Used
1. pandas
-Used to read CSV files and manipulate data.
-Key functions used:
   pd.read_csv() → Read the dataset from CSV.
  .fillna() → Fill missing values in columns.
  .tolist() → Convert column values to a Python list.
  .index[] → Get index of a row.
   
2. scikit-learn (sklearn)
  TfidfVectorizer → Converts text (Genre + Overview) into numerical TF-IDF vectors.
    TF-IDF = Term Frequency – Inverse Document Frequency.
    Words appearing frequently in a document but rarely in all documents get higher weight.
  cosine_similarity → Measures similarity between TF-IDF vectors.
    Cosine similarity value ranges from 0 to 1.
    1 → perfectly similar, 0 → completely dissimilar.

3.fuzzywuzzy
  Handles typos and approximate matches in user input.
  Functions:
    process.extractOne(input, choices) → Finds the closest match from a list of titles.
    Helps user enter partial or misspelled movie names.
##Dataset
  The dataset is a CSV file (imdb_top_1000.csv) with columns:
"Poster_Link,Series_Title,Released_Year,Certificate,Runtime,Genre,IMDB_Rating,Overview,Meta_score,Director,Star1,Star2,Star3,Star4,No_of_Votes,Gross"

**Important columns for recommendation:
    Series_Title → Movie name (user input matches with this)
    Genre → Movie genres
    Overview → Short description of the movie
    IMDB_Rating → Shows rating to display with recommendations
    Poster_Link → URL of the movie poster for visual display
********************************************************************************************************************
    
