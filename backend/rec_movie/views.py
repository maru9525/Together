import json
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from .models import (Movie, Review, Genre, MovieGenre, Provider, MovieProvider)


# Create your views here.
def getMovieData(self):
    # movies = []
    # movie = {"model": "rec_movie.movie", "fields": {}}

    with open('./rec_movie/data/movies.json', 'r') as f:
        data = json.loads(f.read())
    df = pd.json_normalize(data)
    for idx, row in df.iterrows():
        # release_date가 없는 영화가 1개 있다.
        if row['fields.release_date'] == '' or row['fields.poster_path'] is None:
            continue
        Movie.objects.create(movie_id=row['pk'], original_title=row['fields.original_title'],
                             overview=row['fields.overview'], release_date=row['fields.release_date'],
                             poster_path=row['fields.poster_path'])
    return HttpResponse('')


def getReviewData(request):
    with open('./rec_movie/data/movie_reviews.json', 'r') as f:
        data = json.loads(f.read())
    df = pd.json_normalize(data)
    for idx, row in df.iterrows():
        movie = Movie.objects.get(movie_id=row['movieId'])
        Review.objects.create(user_id=row['userId'], Movie=movie, rating=row['rating'])

    return HttpResponse('')



