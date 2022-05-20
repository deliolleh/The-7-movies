from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import Review
from movie.models import Movie

class ReivewSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('제목')

    class Userserializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = 'username'
    
    영화 = MovieSerializer(read_only=True)
    글쓴이 = Userserializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'