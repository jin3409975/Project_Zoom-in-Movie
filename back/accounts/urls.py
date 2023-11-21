from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user/<int:userId>/', views.user),
]
