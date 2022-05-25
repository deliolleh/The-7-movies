from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from movie.models import Movie, Genre
from community.models import Review, Comment

# Create your models here.
class User(AbstractUser):
    like_movies = models.ManyToManyField(Movie, related_name='like_people')
    like_reviews = models.ManyToManyField(Review, related_name='like_people')
    like_comments = models.ManyToManyField(Comment, related_name='like_people')
    genre_status = models.ManyToManyField(Genre, related_name='like_people', through='Genre_score')

class Genre_score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.score)

# class Genre(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_genre')
#     액션 = models.IntegerField(default=0)
#     모험 = models.IntegerField(default=0)
#     애니메이션 = models.IntegerField(default=0)
#     코미디 = models.IntegerField(default=0)
#     범죄 = models.IntegerField(default=0)
#     다큐멘터리 = models.IntegerField(default=0)
#     드라마 = models.IntegerField(default=0)
#     가족 = models.IntegerField(default=0)
#     판타지 = models.IntegerField(default=0)
#     역사 = models.IntegerField(default=0)
#     공포 = models.IntegerField(default=0)
#     음악 = models.IntegerField(default=0)
#     미스터리 = models.IntegerField(default=0)
#     로맨스 = models.IntegerField(default=0)
#     SF = models.IntegerField(default=0)
#     TV_영화 = models.IntegerField(default=0)
#     스릴러 = models.IntegerField(default=0)
#     전쟁 = models.IntegerField(default=0)
#     서부 = models.IntegerField(default=0)