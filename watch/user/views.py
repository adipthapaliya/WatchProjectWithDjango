from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout

from item.models import ProductModel




# Create your views here.

def index(request):
    return render(request,'user/index.html')

def about(request):
    return render(request,'user/about.html')

def contact(request):
    return render(request,'user/contactUs.html')

def login(request):
    return render(request,'user/login_register/login.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']    
        
        user = authenticate(request,username=username, password=password)

        if user is not None:
            log(request,user)
            return redirect('/home')

        else:
            return render(request, '404.html', status=404)

    else:
        return render(request, '404.html', status=404)


def register(request):
    return render(request,'user/login_register/register.html')

# To register User

def register_user(request):
    if request.method == "POST":
        User.objects.create_user(
            first_name = request.POST['fullname'],
            username = request.POST['username'],
            password = request.POST['password'],
            email = request.POST['phonenumber'],

        )
        return redirect('/user/login')
    


    else:
        return render(request, '404.html', status=404)

def log_out(request):
    logout(request)
    return redirect('/home')


def shop(request):
    product= ProductModel.objects.all()
    return render(request,'user/shop.html',{'product' : product})