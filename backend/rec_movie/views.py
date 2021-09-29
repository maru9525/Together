import json
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from .models import (Movie, Review, Genre, MovieGenre, Provider)


# Create your views here.
def get_movie_data(self):
    movie_id_set = set()    # 영화 데이터 중 movie_id를 저장할 set
    with open('./rec_movie/data/movies_kr.json', 'r') as f:
        data = json.loads(f.read())
    df = pd.json_normalize(data)
    for idx, row in df.iterrows():
        # 중복된 영화가 등록 되는지 확인
        if row['pk'] in movie_id_set:
            continue
        movie_id_set.add(row['pk'])

        # release_date가 없는 영화가 1개 있다.
        if row['fields.release_date'] == '' or row['fields.release_date'] is None or row['fields.poster_path'] is None:
            continue
        Movie.objects.create(movie_id=row['pk'], original_title=row['fields.original_title'],
                             overview=row['fields.overview'], release_date=row['fields.release_date'],
                             poster_path=row['fields.poster_path'])
    return HttpResponse('Success convert json to database')


def get_review_data(request):
    with open('./rec_movie/data/movie_reviews.json', 'r') as f:
        data = json.loads(f.read())
    df = pd.json_normalize(data)
    for idx, row in df.iterrows():
        try:
            movie = Movie.objects.get(movie_id=row['movieId'])
        except Movie.DoesNotExist:
            print(f"{row['movieId']}는 존재하지 않습니다.")
        Review.objects.create(user_id=row['userId'], movie_id=movie, rating=row['rating'])

    return HttpResponse('Success convert json to database')


def get_genre_data(self):
    with open('./rec_movie/data/movies_genre.json', 'r') as f:
        data = json.loads(f.read())
    df = pd.json_normalize(data)

    for idx, row in df.iterrows():
        Genre.objects.create(genre_id=row['pk'], genre_name=row['fields.name'])

    return HttpResponse('Success convert json to database')


def get_provider_data(self):
    with open('./rec_movie/data/movies_kr.json', 'r') as f:
        data = json.loads(f.read())

    df = pd.json_normalize(data)
    df = df.fillna(0)

    for idx, row in df.iterrows():

        if row['fields.provider.buy'] != 0:
            Provider.objects.create(movie_id=row['pk'], provider_name=row['fields.provider.buy'][0]['provider_name'])
            # provider_set.add(row['fields.provider.buy'][0]['provider_name'])
        if row['fields.provider.rent'] != 0:
            pass
            Provider.objects.create(movie_id=row['pk'], provider_name=row['fields.provider.rent'][0]['provider_name'])
            # provider_set.add(row['fields.provider.rent'][0]['provider_name'])
        if row['fields.provider.flatrate'] != 0:
            pass
            Provider.objects.create(movie_id=row['pk'], provider_name=row['fields.provider.flatrate'][0]['provider_name'])
            # provider_set.add(row['fields.provider.flatrate'][0]['provider_name'])

    return HttpResponse('Success convert json to database')
