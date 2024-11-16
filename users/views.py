
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.urls import reverse


def user_login(request):
    if request.method== "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('entrepreneur/entrepreneur.html')
            else:
                return HttpResponse("<h1>Incorrect Info</h1>")
        else:
            return HttpResponse("<h1>Incorrect Info</h1>")
    
    else:
        pass

    return render(request,'users/login.html')





@login_required(login_url='login')
def profile(request):
    return render(request, 'entrepreneur:entrepreneur.html')