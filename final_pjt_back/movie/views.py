import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

from accounts.serializers import ProfileSerializer

from .models import Movie, Score, Genre
from accounts.models import Genre_score

from .serializers import MovieChoiceSerializer, MovieMainSerializer, SerachMovieSerializer, movielistserializer, movieserializer, UserGenreSerializer, ScoreSerializer
from accounts.serializers import GenreScoreSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = movielistserializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_paginator(request, movie_page):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 8)
    page_number = movie_page
    page_obj = paginator.get_page(page_number)

    serializer = movielistserializer(page_obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list_filter(request, genre_pk):
    movies = Movie.objects.all().filter(genres__in=genre_pk)
    print(movies)
    serializer = movielistserializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def give_movie_data(request):
    movies = get_list_or_404(Movie)
    serializer = SerachMovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def main_movie(request):
    # movies = Movie.objects.annotate(
    #     total = (F('vote_score')) / (F('popularity') * 100 + Count('vote_user'))
    # ).order_by('total')[0:5]
    # print(movies.values('vote_user'))
    movies = Movie.objects.all().order_by('-vote_count')[1:22:3]
    serializer = MovieMainSerializer(movies, many=True)
    # print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = movieserializer(movie)
    return Response(serializer.data)

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def score_add_change_delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    genres = Genre.objects.filter(movies=movie_pk)
    # print(genres.values())
    if request.method == 'POST':
        score = Score.objects.filter(user=request.user, movie=movie_pk)
        if not score:
            print('create')
            data = { 'score': request.data['score'] }
            serializer = ScoreSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, movie=movie)
    
        else:
            scored = score.values('score')[0]
            print('update')
            # print(user_genres)
            for genre in genres.values():
                user_genre = Genre_score.objects.filter(user=request.user, genre=genre['id']).values_list('genre_id', 'score')
                print(user_genre)
                update_user = Genre_score.objects.get(user=request.user, genre=genre['id'])
                update_user.score -= scored['score']
                update_user.save()
            print('complete')
            # data = { 'score': request.data['score'] }
            now = Score.objects.get(user=request.user, movie=movie_pk)
            # serializer = ScoreSerializer(now)
            serializer = ScoreSerializer(instance=now, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        
        for genre in genres.values():
            user_genre = Genre_score.objects.filter(user=request.user, genre=genre['id']).values_list('genre_id', 'score')
            print(user_genre)
            update_user = Genre_score.objects.get(user=request.user, genre=genre['id'])
            update_user.score += request.data['score']
            update_user.save()
        print('update user_status')

        user = get_user_model().objects.get(pk=request.user.pk)
        send_serializer = ProfileSerializer(user)
        return Response(send_serializer.data)

    elif request.method == 'DELETE':
        score = Score.objects.filter(user=request.user, movie=movie_pk)
        scored = score.values('score')[0]
        print('update')
        # print(user_genres)
        for genre in genres.values():
            user_genre = Genre_score.objects.filter(user=request.user, genre=genre['id']).values_list('genre_id', 'score')
            print(user_genre)
            update_user = Genre_score.objects.get(user=request.user, genre=genre['id'])
            update_user.score -= scored['score']
            print(scored['score'])
            update_user.save()
        score.delete()
        user = get_user_model().objects.get(pk=request.user.pk)
        send_serializer = ProfileSerializer(user)
        return Response(send_serializer.data)

    # 평점 보낼 때 10배해서 보내달라 이야기하기
    # variablerouting이 int로 밖에 못받아서

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def inital_movie(request):
    if request.method == 'GET':
        ran = random.randrange(1, 100)
        movie = Movie.objects.all().order_by('-popularity')[ran + 0:ran + 16]
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
        movies = get_list_or_404(Movie.objects.filter(genres__in=[user[idx].genre_id]).order_by('-vote_score'))[0:num]
        # movies = Movie.objects.filter(genres__in=[user[idx].genre_id]).order_by('-popularity')[0:num]
        # print(movies)
        total += movies
    total = list(set(total))
    random.shuffle(total)
    total = total[0:7]
    
    serializer = movielistserializer(total, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if movie.like_people.filter(pk=request.user.pk):
        movie.like_people.remove(request.user)
    
    else:
        movie.like_people.add(request.user)

    serializer = movieserializer(movie)
    print(serializer.data)
    return Response(serializer.data)
