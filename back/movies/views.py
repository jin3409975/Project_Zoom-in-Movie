from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from .models import Movie, Comment, Genre, Actor
from .serializers import MovieListSerializer, CommentListSerializer, MovieSerializer, GenreListSerializer
from accounts.serializers import UserSerializer
from random import sample



### 영화 목록 ###
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        seralizer = MovieListSerializer(movies, many=True)
        return Response(seralizer.data)
        

### 영화 상세 ###        
@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, movie_id=movie_pk)
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)
            

### 댓글 목록 ###        
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)


### 댓글 생성 및 목록 조회 ###
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movieId = get_object_or_404(Movie, movie_id=movie_pk).id
    if request.method == 'GET':
        comments = Comment.objects.filter(movie_id=movieId)
        seralizer = CommentListSerializer(comments, many=True)
        return Response(seralizer.data)
      
    if request.method == 'POST':
        serializer = CommentListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movieId, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


### 댓글 조회, 수정, 삭제 ###    
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
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



### 영화 추천 알고리즘 ###
@api_view(['POST'])
def recommend(request):
  favorite_movies = Movie.objects.all().order_by('-rating')[:30]
  serializer_1 = MovieSerializer(favorite_movies, many=True)
  shortest_movies = Movie.objects.all().order_by('runtime')[30:60]
  serializer_2 = MovieSerializer(shortest_movies, many=True)
  
  # 좋아요 기반
  users_movies = set()
  # like_movies = request.data.get('like_movies')
  User = request.user
  my_genres = {}
  my_movies = []
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

    movies = get_list_or_404(Movie)
    recommendations_list = set()
    for my_genre in my_genres:
        for movie in movies:
            genres = movie.genres.all()
            for genre in genres:
                if genre.pk == my_genre:
                    recommendations_list.add(movie)
                    break
    
    recommendations_list = list(recommendations_list)
    recommendations = sorted(recommendations_list, key=lambda x: x.popularity, reverse=True)[:30]

    serializer_3 = MovieSerializer(users_movies, many=True)
    serializer_4 = MovieSerializer(recommendations, many=True)
    return Response([serializer_1.data, serializer_2.data, serializer_3.data, serializer_4.data])
  else:
    serializer_3 = MovieSerializer(users_movies, many=True)
    return Response([serializer_1.data, serializer_2.data, serializer_3.data, []])


### 영화 좋아요 ###
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


### 좋아요 누른 영화 ##
@api_view(['POST'])
def is_liked(request, my_pk, movie_id):
  movie = get_object_or_404(Movie, movie_id=movie_id)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      liking = True
  else:
      liking = False
  return Response(liking)


### 해당 사용자가 좋아요 누른 영화 ###
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


### 해당 영화에 좋아요 누른 사용자들 ###
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


### 해당 사용자가 좋아요 누른 영화들 ###
#
@api_view(['post'])
def user_like_movies(request, user_pk):
  like_movies_id = request.data.get('like_movies')
  comment_ids = request.data.get('comments')
  movies = Movie.objects.all()

  comment_movie_id = []
  for comment_id in comment_ids:
    comment =Comment.objects.get(pk=comment_id)
    comment_movie_id.append(comment.movie_id)

  comment_movies = []
  like_movies = []
  for movie in movies:
    if movie.pk in like_movies_id:
      like_movies.append(movie)
    if movie.pk in comment_movie_id:
      comment_movies.append(movie)
  serializers = MovieSerializer(like_movies, many=True)
  comment_serializers = MovieSerializer(comment_movies, many=True)
  return Response([serializers.data, comment_serializers.data])


### 사용자 정보 ###
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


### 추천받은 영화 ###
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
    else:
      movies = get_list_or_404(Movie)
      recommendations = sample(movies, 20)
      serializer = MovieSerializer(recommendations, many=True)

    return Response(serializer.data)
  else:
    movies = get_list_or_404(Movie)
    recommendations = sample(movies, 10)
    serializer = MovieSerializer(recommendations)


### 현재 인기도 (상위 30개) ### 
@api_view(['GET'])
def current_popularity(request):
  if request.method == 'GET':
    movies = Movie.objects.order_by('-popularity')[:30]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  
### 장르 목록 ###
@api_view(['GET'])
def genres(request):
    if request.method == 'GET':
        genres = get_list_or_404(Genre)
        seralizer = GenreListSerializer(genres, many=True)
        return Response(seralizer.data)
      

### 장르별 영화 조회 ###
@api_view(['GET'])
def genre(request, genre):
    if request.method == 'GET':
        genreId = get_object_or_404(Genre, genre_name=genre).genre_id
        movies = Movie.objects.filter(genres=genreId).order_by('-popularity')
        if len(movies) > 1:
          seralizer = MovieListSerializer(movies, many=True)
        else:
          seralizer = MovieListSerializer(movies)
        return Response(seralizer.data)