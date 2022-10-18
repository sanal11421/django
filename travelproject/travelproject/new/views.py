from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid new")
            return redirect('login')
    return render(request,"login.html")
def register(request, last_name=None):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['First_Name']
        last_name = request.POST['last_name']
        email = request.POST['Email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                print("Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                print("email Taken")
                return redirect('register')
            user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
            user.save();
            return redirect('login')
            print("register")

        else:

            messages.info(request, "password incorrect")
            print("password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')