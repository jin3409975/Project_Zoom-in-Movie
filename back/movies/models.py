from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# from ..accounts

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
class Actor(models.Model):
    name = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    release_date = models.DateTimeField()
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_movies'
    )
    rating = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    image = models.CharField(max_length=255)


class Comment(models.Model):
    # content = var
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)