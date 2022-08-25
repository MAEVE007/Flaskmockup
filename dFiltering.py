import pandas as pd
import numpy as np
import csv

df = pd.read_csv('final.csv')

C = df['vote_average'].mean()
m = df['vote_count'].quantile(0.9)
q_movies = df.copy().loc[df['vote_count'] >= m]

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)

output = q_movies[['title', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].head(20)
print(output.values.tolist())
print(len(output))
# with open("movies20.csv","w",encoding="utf8") as f:
#     csvwriter =csv.writer(f)
#     csvwriter.writerows(output)