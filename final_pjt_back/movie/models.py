from enum import unique
from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

class Movie(models.Model) :
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)
    popularity = models.FloatField()
    vote_score = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    director = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre, related_name='movies')
    vote_user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Score')

    def __str__(self):
        return self.title

class Actor(models.Model):
    movie = models.ForeignKey(Movie, related_name='actors', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Score(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields= ["movie", "user"],
                name = "unique vote",
            ),
        ]