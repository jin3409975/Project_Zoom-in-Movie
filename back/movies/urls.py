from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('comments/', views.comment_list),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('movies/<int:movie_pk>/comment/', views.comment_create),
]
