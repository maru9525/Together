import json
import pandas as pd
from django.http import (HttpResponse, Http404)
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.generics import GenericAPIView
from rest_framework_swagger import renderers
from rest_framework.response import Response

from .models import (Movie, Review, Genre, Provider)
from .serializers import (MovieSerializer, ReviewSerializer, GenreSerializer, ProviderSerializer)

# @api_view(['GET'])
# @renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def convert_movie_data(self):
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
        movie = Movie.objects.create(movie_id=row['pk'], original_title=row['fields.original_title'],
                                     overview=row['fields.overview'], release_date=row['fields.release_date'],
                                     poster_path=row['fields.poster_path'])
        for genre_id in row['fields.genre_ids']:
            genre = Genre.objects.get(genre_id=genre_id)
            movie.genres.add(genre)

    return HttpResponse('Success convert json to database')


def convert_review_data(request):
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


def convert_genre_data(self):
    with open('./rec_movie/data/movies_genre.json', 'r') as f:
        data = json.loads(f.read())
    df = pd.json_normalize(data)

    for idx, row in df.iterrows():
        Genre.objects.create(genre_id=row['pk'], genre_name=row['fields.name'])

    return HttpResponse('Success convert json to database')


def convert_provider_data(self):
    with open('./rec_movie/data/movies_kr.json', 'r') as f:
        data = json.loads(f.read())

    df = pd.json_normalize(data)
    df = df.fillna(0)

    for idx, row in df.iterrows():
        try:
            movie = Movie.objects.get(movie_id=row['pk'])
        except Movie.DoesNotExist:
            print(f"{row['pk']}는 존재하지 않습니다.")

        provider_set = set()
        if row['fields.provider.buy'] != 0:
            provider_list_to_set(provider_set, row['fields.provider.buy'])
        if row['fields.provider.rent'] != 0:
            provider_list_to_set(provider_set, row['fields.provider.rent'])
        if row['fields.provider.flatrate'] != 0:
            provider_list_to_set(provider_set, row['fields.provider.flatrate'])

        for provider in provider_set:
            Provider.objects.create(movie_id=movie, provider_name=provider)

    return HttpResponse('Success convert json to database')


# row['fields.provider']에는 중복되는 provider가 있으므로, set을 통해 중복을 제거해준다.
def provider_list_to_set(p_set, p_list):
    size = len(p_list)
    for idx in range(0, size):
        p_set.add(p_list[idx]['provider_name'])


def post(self, request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Review CRUD
class ReviewView(GenericAPIView):
    queryset = Review.objects.all()  # Generic Api View는 반드시 포함 해야함
    serializer_class = ReviewSerializer

    def post(self, request, format=None):
        """
        리뷰를 등록하기 위한 API입니다.

        ---
        # Parameters
            - user_id : 유지 id(닉네임)
            - rating : 평가 점수 (0 ~ 10)
            - movie_id : 연계된 movie. movie의 primary key와 연결해야한다.

        responseMessages:
            - code: 201
              message: Success Create Album

        """

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailView(GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_object_review(self, pk):
        try:
            return Review.objects.get(id=pk)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        review = self.get_object_review(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        review = self.get_object_review(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        review = self.get_object_review(pk)
        review.delete()
        try:
            return Response(status=status.HTTP_200_OK)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)