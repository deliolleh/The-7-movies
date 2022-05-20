from django.urls import path
from . import views

urlpatterns = [
    path('profile/init', views.user_init),
    path('profile/<username>', views.profile),
]
