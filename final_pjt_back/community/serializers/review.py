from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import Review, Comment
from movie.models import Movie

class ReivewListSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('제목',)

    class Userserializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('username',)
    
    영화 = MovieSerializer(read_only=True)
    글쓴이 = Userserializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            exclude = ('review',)
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk',)

    comment_set = CommentSerializer(many=True, read_only=True)
    like_people = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('title', 'content', 'comment_set', 'like_people')
        read_only = ('comment_set',)

