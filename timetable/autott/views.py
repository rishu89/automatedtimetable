from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    return HttpResponse("<h1>This is just a homepage")

"""def user_login(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(username=phone, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/autott/home')
        else:
            error = "Sorry! Phone number or password didn't match, Please try again !"
            return render(request, 'login.html',{'error':error})
    else:
        return render(request, 'login.html')

def user_signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass_1 = request.POST.get('password1')
        pass_2 = request.POST.get('password2')
        if pass_1 == pass_2:
            user = User.objects.create_user(
                username=phone,
                email=email,
                password=pass_1,
                )
            return HttpResponseRedirect("/")
        else:
            error = "Password Mismatch"
            return render(request, 'signup.html',{"error":error})
    else:
        return render(request,'signup.html')
"""