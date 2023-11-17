from django.db import models
from django.conf import settings


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    genre_name = models.CharField(max_length=20)
    
    
class Actor(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    movie_id = models.TextField()
    title = models.TextField()
    original_title = models.TextField()
    overview = models.TextField()
    poster_path = models.TextField()
    rating = models.FloatField()
    release_date = models.TextField()
    runtime = models.IntegerField()
    popularity = models.FloatField()
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=500)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_movies'
    )
    genres = models.ManyToManyField(
        Genre, related_name='genre_movie'
    )
    actors = models.ManyToManyField(
        Actor, related_name='actor_movie'
    )


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)