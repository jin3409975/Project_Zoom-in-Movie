from rest_framework import serializers
from .models import Movie, Comment, Genre, Actor


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('id', 'movie_id', 'title', 'original_title', 
        #           'overview', 'rating', 'release_date', 'runtime',
        #           'popularity', 'adult', 'genres', 'actors',
        #           'like_users',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_movies', 'like_users',)
        
        
class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
        
class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


