import imp
import re
from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout

from item.models import ProductModel
from adminapp.form import MessageForm
from adminapp.models import MessageModel



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

def message(request):
    message = MessageModel.objects.all()
    return render(request,'admin/message.html',{'message':message})

def getmessage(request):
    data = MessageForm(request.POST)
    data.save()

    return redirect('/contact') 


