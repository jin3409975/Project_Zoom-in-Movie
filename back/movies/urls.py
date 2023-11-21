from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('comments/', views.comment_list),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('movies/<int:movie_pk>/comment/', views.comment_create),

    path('recommend/', views.recommend),
    path('<int:my_pk>/<int:movie_id>/like/', views.movie_like),
    path('<int:my_pk>/<int:movie_id>/is_liked/', views.is_liked),
    path('<int:my_pk>/like/', views.my_movie_like),
    path('<int:my_pk>/like/users/', views.like_movie_users),
    
    #
    path('<int:user_pk>/like/comment/', views.user_like_movies),

    path('info/', views.users_info),

    path('recommended/', views.recommended, name='recommended'),
    path('current_popularity/', views.current_popularity),
    path('genres/', views.genres),
    path('genre/<genre>/', views.genre),
]
