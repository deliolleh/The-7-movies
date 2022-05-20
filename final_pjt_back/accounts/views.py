from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import GenreSerializer


# Create your views here.
def user_init(request):
    serializer = GenreSerializer(data=request.data)
    return Response(serializer.data)

def profile(request, username):
    pass