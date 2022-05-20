from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list),
    path('create/', views.create_review),
    path('detail/<int:review_pk>', views.review_detail),
    path('detail/<int:review_pk>/like', views.like_review),
    path('detail/<int:review_pk>/comment', views.create_comment),
    
    # axios요청시 comment_pk 보내달라고 이야기할 것
    path('detail/<int:review_pk>/<int:comment_pk>', views.update_delete_comment),
    path('detail/<int:review_pk>/<int:comment_pk>/like', views.like_comment),
]
