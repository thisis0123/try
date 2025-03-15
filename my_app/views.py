from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def sign_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if 'next' in request.POST:
                return redirect('my_videos:videos')
            else:
                return redirect('/')
            
        else:
            messages.info(request,'Sorry, your password or username is wrong!')
            return redirect('users:signin')

    else:
        return render(request,'users/sign-in.html')



def sign_up(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Sorry, there is a user with this name!')
            return redirect('users:signup')
        else:
            if password==password2:
                user= User.objects.create(username=username,password=password)
                user.set_password(password)
                user.save()
                login(request,user)
                return redirect('/')
            
            else:
                messages.info(request,'The passwords do not match!')
                return redirect('users:signup')



    else:
        return render(request,'users/sign-up.html')
    



def logout_user(request):
    if request.method=='POST':
        logout(request)
        return redirect('/')
