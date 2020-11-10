from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def sign_up(request):
    context = {}

    # POST Method
    if request.method == 'POST': #http 메소드가 POST일때의 로직
        if (request.POST['username'] and
                request.POST['password'] and
                request.POST['password'] == request.POST['password_check']):

            new_user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            ) 

            auth.login(request, new_user)
            return redirect('posts:index')#회원가입뒤 자동로그인기능

        else: 
            context['error'] = '아이디와 비밀번호를 다시 확인해줴요.'

    # GET Method #http 메소드가 GET일때의 로직  , else가 생략됨
    return render(request, 'accounts/sign_up.html', context)


def login(request):
    context = {}

    # POST Method
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:

            user = auth.authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password']
            )

            if user is not None:
                auth.login(request, user)
                return redirect('posts:index')
            else:
                context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'

        else:
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요.'

    # GET Method
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('posts:index')


