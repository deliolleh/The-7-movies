from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import Review, Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content',)