from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import Review, Comment
from movie.models import Movie

class ReivewListSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title', 'pk')

    class Userserializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('username',)
    
    movie = MovieSerializer(read_only=True)
    user = Userserializer(read_only=True)
    like_people = Userserializer(many=True, read_only=True)
    like_count = serializers.IntegerField()
    comment_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('pk', 'movie', 'user', 'title', 'content', 
                'created_at', 'updated_at', 'comments',
                'like_people', 'like_count', 'comment_count')


class ReviewSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            exclude = ('review',)
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk',)

    comments = CommentSerializer(many=True, read_only=True)
    like_people = UserSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('movie', 'user', 'title', 'content', 
                'created_at', 'updated_at', 'comments',
                'like_people', 'like_count')
        read_only_fields = ('comment_set', 'movie', 'user', 'like_count')


class ReviewCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('user', 'movie', 'title', 'content')
        read_only_fields = ('user',)