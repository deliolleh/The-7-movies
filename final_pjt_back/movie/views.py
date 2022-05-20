import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Movie, Genre, Actor

from .serializers import MovieChoiceSerializer, movielistserializer, movieserializer, UserGenreSerializer
from movie import serializers

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = movielistserializer(movies, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializers = movieserializer(movie)
    return Response(serializers.data)

@api_view(['POST', 'PUT', 'DELETE'])
def scroe_add_change_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 평점 보낼 때 10배해서 보내달라 이야기하기
    # variablerouting이 int로 밖에 못받아서
    request.data
    score = float(int / 10)
    def regist_score(score):
        movie.user_vote = score
    
    def change_score(score):
        movie.user_vote = score

    def delete_score(score):
        pass

    if request.method == 'POST':
        regist_score(score)
    
    elif request.method == 'PUT':
        change_score(score)
    
    elif request.method == 'DELETE':
        delete_score(score)

@api_view(['GET', 'POST'])
def inital_movie(request, username):
    if request.method == 'GET':
        movie = get_list_or_404(Movie)[0:50]
        movie = random.sample(movie, 16)
        serializer = MovieChoiceSerializer(movie, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # request.POST
        user = get_object_or_404(get_user_model(), username=username)
        serializer = UserGenreSerializer(user)