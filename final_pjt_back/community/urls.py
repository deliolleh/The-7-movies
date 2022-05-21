from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list),
    path('create/', views.create_review),
    path('<int:review_pk>/', views.review_detail),
    path('<int:review_pk>/like/', views.like_review),
    path('<int:review_pk>/comment/', views.create_comment),
    path('<review_name>/', views.serach_review),
    
    # axios요청시 comment_pk 보내달라고 이야기할 것
    path('<int:review_pk>/<int:comment_pk>/', views.update_delete_comment),
    # path('<int:review_pk>/<int:comment_pk>/like', views.like_comment),
]
