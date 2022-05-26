from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list), #
    path('moviepage/<int:movie_page>/', views.movie_paginator),
    path('filter/<int:genre_pk>/', views.movie_list_filter),
    path('popular/', views.main_movie), #
    path('<int:movie_pk>/', views.movie_detail), #
    path('<int:movie_pk>/score/', views.score_add_change_delete), #
    path('<int:movie_pk>/like/', views.like_movie), #
    path('recommends/', views.recommends), #
    path('review/search/', views.give_movie_data), #
    path('recommends/representative/', views.inital_movie), #
]