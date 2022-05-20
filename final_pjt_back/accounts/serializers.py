from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Review, Comment
# from .models import Genre


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

    review_set = ReviewSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'like_movies', 'like_reviews', 'like_comments', 'review_set', 'comment_set')
    
    