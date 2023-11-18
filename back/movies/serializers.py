from rest_framework import serializers
from .models import Movie, Comment, Genre, Actor


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_movies', 'like_users',)
        
        
class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('Movie', 'user',)


