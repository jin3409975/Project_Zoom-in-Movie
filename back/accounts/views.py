from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


# Create your views here.

@api_view(['POST'])
def signup(request):
    # Client 에서 보내온 정보 받기
    password = request.data.get('password')
    passwordConfirmation = request.data.get('passwordConfirmation')
    # 비밀번호 일치 여부 확인
    if password != passwordConfirmation:
        return Response({ 'error': '비밀번호가 일치하지 않습니다.'})

    # 사용자가 보낸 데이터로 UserSerializer 를 통해 데이터 생성
    else:
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # 그냥 저장하고 끝내면 비밀번호 유출
            user = serializer.save()

            # 비밀번호 해싱
            user.set_password(request.data.get('password'))
            user.save()

            return Response(serializer.data)



@api_view(['GET', 'POST'])   # GET 또는 POST로만 호출 가능
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:   # GET
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)



@api_view(['POST'])
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


@login_required
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')
