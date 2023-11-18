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
def like_movie_users(request, my_pk):
  users = []
  user = get_object_or_404(get_user_model(), pk=my_pk)
  movies = user.like_movies.all()
  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie.pk)
    serializer = MovieSerializer(movie)
    for user in serializer.data.get('like_users'):
      if user not in users:
        users.append(user)

  return Response(users)



@api_view(['post'])
def user_like_movies(request, user_pk):
  like_movies_id = request.data.get('like_movies')
  review_ids = request.data.get('reviews')
  movies = Movie.objects.all()

  review_movie_id = []
  for review_id in review_ids:
    review = Review.objects.get(pk=review_id)
    review_movie_id.append(review.movie_id)

  review_movies = []
  like_movies = []
  for movie in movies:
    if movie.pk in like_movies_id:
      like_movies.append(movie)
    if movie.pk in review_movie_id:
      review_movies.append(movie)
  serializers = MovieSerializer(like_movies, many=True)
  review_serializers = MovieSerializer(review_movies, many=True)
  return Response([serializers.data, review_serializers.data])


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



@api_view(['GET'])
def recommended(request):
  if request.user.is_authenticated:
    movies = get_list_or_404(Movie)
    User = request.user
    my_genres = {}
    my_movies = User.like_movies.all()
    
    if my_movies:
      for movie in my_movies:
          genres = movie.genres.all()
          for genre in genres:
              if genre.pk in my_genres:
                  my_genres[genre.pk] += 1
              else:
                  my_genres[genre.pk] = 1

      my_genres = sorted(my_genres, key=lambda x: my_genres[x])[:3]

      recommendations_list = set()
      for my_genre in my_genres:
          for movie in movies:
              genres = movie.genres.all()
              for genre in genres:
                  if genre.pk == my_genre:
                      recommendations_list.add(movie)
                      break
      recommendations = sample(recommendations_list, 20)
      serializer = MovieSerializer(recommendations)
      # liked = True
    else:
      movies = get_list_or_404(Movie)
      recommendations = sample(movies, 20)
      serializer = MovieSerializer(recommendations, many=True)
      # liked = False

    return Response(serializer.data)
  else:
    movies = get_list_or_404(Movie)
    recommendations = sample(movies, 10)
    serializer = MovieSerializer(recommendations)
