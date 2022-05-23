from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Review, Comment
from movie.models import Score
from .models import Genre_score


# class GenreSerializer(serializers.ModelSerializer):

#         class Meta:
#             model = Genre
#             fields = '__all__'


# class ProfileSerializer(serializers.ModelSerializer):

#     class ReviewSerializer(serializers.ModelSerializer):
        
#         class Meta:
#             model = Review
#             fields = ('pk', 'title', 'content')

#     user_genre = GenreSerializer(read_only=True)

#     class Meta:
#         model = get_user_model()
#         fields = ('pk', 'username', 'email', 'like_articles', 'articles',)

class ProfileSerializer(serializers.ModelSerializer):
    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('pk', 'title', 'content')
    
    class CommentSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Comment
            fields = '__all__'

    class GenreScoreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre_score
            fields = ('genre', 'score',)
    
    class ScoreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Score
            exclude = ('pk',)

    like_reviews = ReviewSerializer(many=True, read_only=True)
    like_comments = CommentSerializer(many=True, read_only=True)
    genre_score_set = GenreScoreSerializer(many=True, read_only=True)
    score_set = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'like_movies',
            'like_reviews', 'like_comments', 'review_set',
            'comment_set', 'genre_score_set', 'score_set')
        read_only_fields = ('user',)


class GenreScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre_score
        fields = '__all__'
        read_only_fields = ('user', 'genre')