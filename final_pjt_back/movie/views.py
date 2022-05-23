import random

from django.db.models import F, Count

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Movie, Score
from accounts.models import Genre_score

from .serializers import MovieChoiceSerializer, MovieMainSerializer, SerachMovieSerializer, movielistserializer, movieserializer, UserGenreSerializer, ScoreSerializer
from accounts.serializers import GenreScoreSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = get_list_or_404(Movie)
    print(movies)
    serializer = movielistserializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def give_movie_data(request):
    movies = get_list_or_404(Movie)
    serializer = SerachMovieSerializer(movies, many=True)
    print('hi')
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def main_movie(request):
    movies = Movie.objects.annotate(
        total = (F('vote_score')) / (F('popularity') * 100 + Count('vote_user'))
    ).order_by('total')[0:5]
    # print(movies.values('vote_user'))
    # movies = Movie.objects.all().order_by('-popularity')[0:5]
    serializer = MovieMainSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = movieserializer(movie)
    return Response(serializer.data)

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def scroe_add_change_delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    genres = Movie.objects.filter(pk=movie_pk).values('genres')
    # print(genres)
    if request.method == 'POST':
        score = Score.objects.filter(user=request.user, movie=movie).first()
        if not score:
            # print('create')
            serializer = ScoreSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, movie=movie)
                # 추후 update 부분을 복사
                # for genre in genres:
                #     print(genre['genres'])
                #     status = Genre_score.objects.filter(genre['genres'])
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        else:
            # print('update')
            serializer = ScoreSerializer(instance=score, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # 되는지 체크!
                for genre in genres:
                    status = Genre_score.objects.get(user=request.user, genre=genre['genres'])
                    # print(status.score)
                    data = {
                        "score" : status.score + 5
                    }
                    secondeserializer = GenreScoreSerializer(instance=status, data=data)
                    if secondeserializer.is_valid(raise_exception=True):
                        secondeserializer.save()
                return Response(serializer.data)

    elif request.method == 'DELETE':
        score = Score.objects.filter(user=request.user, movie=movie)
        score.delete()
        data = {
            "message": "정상적으로 삭제되었습니다"
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)

    # 평점 보낼 때 10배해서 보내달라 이야기하기
    # variablerouting이 int로 밖에 못받아서

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def inital_movie(request):
    if request.method == 'GET':
        ran = random.randrange(1, 100)
        movie = Movie.objects.all()[ran + 0: ran + 16]
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
    # user = get_list_or_404(Genre_score.objects.filter(user=request.user).order_by('score'))[0:4]
    user = Genre_score.objects.filter(user=request.user).order_by('-score')[0:4]

    total = []
    for idx in range(len(user)):
        # print(user[idx].genre_id)
        num = 3 if idx != len(user) - 1 else 2
        movies = get_list_or_404(Movie.objects.filter(genres__in=[user[idx].genre_id]).order_by('-popularity'))[0:num]
        # movies = Movie.objects.filter(genres__in=[user[idx].genre_id]).order_by('-popularity')[0:num]
        # print(movies)
        total += movies
    total = list(set(total))[0:7]
    serializer = movielistserializer(total, many=True)
    return Response(serializer.data)
