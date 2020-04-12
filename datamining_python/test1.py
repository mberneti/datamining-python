import json

with open('./movieratings_simple.json') as f:
    movie_rating_simple = json.load(f)

print(movie_rating_simple)
