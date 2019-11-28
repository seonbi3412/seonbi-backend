from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=10)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres', blank=True)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, blank=True)
    birthday = models.TextField(blank=True)
    profile_path = models.TextField(blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actors', blank=True)

class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies')
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=200)
    poster_url = models.TextField()
    description = models.TextField()
    score = models.FloatField()
    open_date = models.DateField()
    director = models.IntegerField(blank=True)
    video = models.TextField(blank=True)
    country = models.TextField(blank=True)
    watchgrade = models.CharField(max_length=15, blank=True)
    actors = models.ManyToManyField(Actor, related_name='filmography', blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)


class RootReview(models.Model):
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Review(RootReview):
    score = models.IntegerField()
    movieName = models.CharField(max_length=150)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Article(RootReview):
    pass
