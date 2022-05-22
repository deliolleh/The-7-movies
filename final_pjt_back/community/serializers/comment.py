from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import Comment, Review

class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    
    # class ReviewSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Review
    #         fields = ('pk',)

    user = UserSerializer(read_only=True)
    # review = ReviewSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'content', 'user', 'review')
        read_only_fields = ('user', 'review')