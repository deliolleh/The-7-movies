from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/<int:score>/', views.scroe_add_change_delete),
    # path('recommends/representative', views.scroe_add_change_delete),
]