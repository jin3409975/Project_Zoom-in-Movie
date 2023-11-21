from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:userId>/', views.get_user),
]
