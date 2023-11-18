from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import Movie, Comment, Genre, Actor
from .serializers import MovieListSerializer, CommentListSerializer
from accounts.serializers import UserSerializer



@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        seralizer = MovieListSerializer(movies, many=True)
        return Response(seralizer.data)
        
        
@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, movie_id=movie_pk)
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)
            
        
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        serializer = CommentListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentListSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentListSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

@api_view(['POST'])
def movie_like(request, my_pk, movie_id):
  movie = get_object_or_404(Movie, movie_id=movie_id)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      liking = False
      
  else:
      me.like_movies.add(movie.pk)
      liking = True
  
  return Response(liking)


@api_view(['POST'])
def my_movie_like(request, my_pk):
  me = get_object_or_404(get_user_model(), pk=my_pk)
  data = []
  movies = me.like_movies.all()
  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie.id)
    serializer = MovieSerializer(movie)
    data.append(serializer.data)
  
  return Response(data)



@api_view(['POST'])
def users_info(request):
  users = request.data.get('users')
  movies = []
  for user in users:
      user = get_object_or_404(get_user_model(), pk=user)
      serializer = UserSerializer(user)
      like_movies = serializer.data.get('like_movies')
      for movie in like_movies:
          if movie not in movies:
              movies.append(movie)
  
  return Response(movies)
