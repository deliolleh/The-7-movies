from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from .serializers import GenreScoreSerializer, ProfileSerializer
from movie.models import Genre
from .models import Genre_score

# from .serializers import GenreSerializer


# Create your views here.
# def user_init(request):
#     serializer = GenreSerializer(data=request.data)
#     return Response(serializer.data)

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@api_view(['Get'])
def genre_init(request):
    genres = Genre.objects.all()
    for genre in genres:
        data= {
            "score" : 0
        }
        serializer = GenreScoreSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, genre=genre)
    data = {
        "message": "성공적으로 초기화됐습니다"
    }
    return Response(data=data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def get_init(request):
    user = Genre_score.objects.filter(user=request.user)
    serializer = GenreScoreSerializer(instance=user, data=request.data, many=True)
    # serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        data = {
            "message": "변경완료"
        }
        return Response(data=data)