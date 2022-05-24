from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre, Actor, Score

class movielistserializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = ('title', 'like_people', 'poster_path', 'pk')
        read_only_fields = ('like_people',)

class SerachMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'poster_path', 'pk')

class MovieMainSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = ('poster_path', 'pk')


class movieserializer(serializers.ModelSerializer):
    class genreserializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = '__all__'

    class actorlistserializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = '__all__'
    
    class scorelistserializer(serializers.ModelSerializer):

        class Meta:
            model = Score
            fields = ('score',)

    class userlistserializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('username',)

    genres = genreserializer(many=True, read_only=True)
    actor = actorlistserializer(many=True, read_only=True)
    score_set = scorelistserializer(many=True, read_only=True)
    like_people = userlistserializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('like_people',)


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = '__all__'
        read_only_fields = ('user', 'movie')


class MovieChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('poster_path', 'title', 'genres')


class UserGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('genre_status',)
        read_only_fiedls = ('genre_status',)