import imp
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout

from item.models import ProductModel




# Create your views here.


def login(request):
    return render(request,'admin/login/login.html')

def index(request):
    return render(request,'admin/index.html')

def item(request):
    product = ProductModel.objects.none()

    return render(request,'admin/additem.html',{'product':product})

def viewitem(request):
    product= ProductModel.objects.all()
    return render(request,'admin/item.html',{'product' : product})


