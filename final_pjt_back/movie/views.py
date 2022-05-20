import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Movie, Genre, Actor

from .serializers import MovieChoiceSerializer, MovieMainSerializer, SerachMovieSerializer, movielistserializer, movieserializer, UserGenreSerializer, ScoreSerializer

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = movielistserializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def give_movie_data(request):
    movies = get_list_or_404(Movie)
    serializer = SerachMovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def main_movie(request):
    movies = Movie.objects.all().order_by('-popularity')[0:5]
    serializer = MovieMainSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializers = movieserializer(movie)
    return Response(serializers.data)

@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def scroe_add_change_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ScoreSerializer(data=request.POST)
    serializer.save()
    return Response(serializer.data)

    # 평점 보낼 때 10배해서 보내달라 이야기하기
    # variablerouting이 int로 밖에 못받아서

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def inital_movie(request):
    if request.method == 'GET':
        movie = get_list_or_404(Movie).order_by('-popularity')[0:50]
        movie = random.sample(movie, 16)
        serializer = MovieChoiceSerializer(movie, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # request.POST
        serializer = UserGenreSerializer(request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommends(request):
    user_status = get_object_or_404(get_user_model(), pk=request.user.pk).genres_status.all()
    user_status = sorted(user_status, key=lambda x: x['score'])[0:4]
    total = []
    for idx in range(len(user_status)):
        num = 2 if idx != len(user_status) - 1 else 1
        movies = Movie.objects.filter(genres__in=[user_status[idx]]).order_by('-popularity')[0:num]
        total.append(movies)
    serializer = movielistserializer(data=total, many=True)
    return Response(serializer.data)


