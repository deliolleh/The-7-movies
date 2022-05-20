from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import ProfileSerializer

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