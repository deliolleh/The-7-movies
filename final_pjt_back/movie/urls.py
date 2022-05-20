from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('review/serach/', views.give_movie_data),
    path('popular/', views.main_movie),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/', views.scroe_add_change_delete),
    path('recommends/representative/', views.inital_movie),
    path('recommends/', views.recommends),
]