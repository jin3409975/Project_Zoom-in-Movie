from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


@api_view(['GET'])
def get_user(request, userId):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(), id=userId)
        serializer = UserSerializer(user)
        return Response(serializer.data)
