from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)\
    
    
class Actor(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    content = models.TextField()
    rating = models.FloatField()
    poster_path = models.CharField(max_length=200)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_movies'
    )
    genre = models.ManyToManyField(
        Genre, related_name='genre_movie'
    )
    actors = models.ManyToManyField(
        Actor, related_name='actor_movie'
    )


class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )