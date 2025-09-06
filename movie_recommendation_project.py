import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process

df = pd.read_csv(r"D:\imdb_top_1000.csv")
df["combined"] = df["Genre"].fillna('') + " " + df["Overview"].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df["combined"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_closest_match(user_input):
    titles = df["Series_Title"].tolist()
    match, score = process.extractOne(user_input, titles)
    if score < 60:
        return None
    return match

def recommend(movie_name, top_n=10):
    match = get_closest_match(movie_name)
    if not match:
        print("Sorry bhai, movie not found!")
        return
    idx = df[df["Series_Title"] == match].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]

    print(f"\nTop {top_n} movies similar to '{df['Series_Title'][idx]}':\n")
    for i, movie_idx in enumerate(movie_indices, 1):
        print(f"{i}. {df['Series_Title'][movie_idx]} "
              f"(IMDB: {df['IMDB_Rating'][movie_idx]}, Genre: {df['Genre'][movie_idx]})")
        print(f"   Poster: {df['Poster_Link'][movie_idx]}\n")

user_movie = input("Enter a movie name: ")
recommend(user_movie, top_n=10)
