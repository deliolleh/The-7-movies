from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router= DefaultRouter()
router.register("reviews", views.ReviewViewSet, basename="reviews")

urlpatterns = [
    path('', views.review_list),
    path('', include(router.urls)),
    path('filter/<int:movie_pk>/', views.filter_reviews),
    path('create/', views.create_review),
    path('<int:review_pk>/', views.review_detail),
    path('<int:review_pk>/like/', views.like_review),
    path('<int:review_pk>/comment/', views.create_comment),
    path('<review_name>/', views.serach_review),
    
    # axios요청시 comment_pk 보내달라고 이야기할 것
    path('<int:review_pk>/<int:comment_pk>/', views.update_delete_comment),
    path('<int:review_pk>/<int:comment_pk>/like/', views.like_comment),
]