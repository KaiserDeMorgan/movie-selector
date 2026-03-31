import pandas as pd

df = pd.read_csv("movie_dataset.csv")
df = df.drop(columns=["index", "budget", "homepage", "id", "production_companies", "production_countries", "spoken_languages", \
                      "revenue", "status", "tagline", "vote_average", "vote_count", "crew"])

df.to_csv("movie_dataset_clean.csv", index=False)