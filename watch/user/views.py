from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout

from item.models import BuyProductModel, ProductModel
from user.models import UserCartModel
from user.form import CartForm




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

def addtocart(request,id,uid):
    data =  UserCartModel(product_id_id=id, user_if_id=uid )
    data.save()

    cart = UserCartModel.objects.filter(user_if_id=id)
    return redirect('/user/cart/1')


def  buynow(request,id,uid):
    data =  BuyProductModel(product_id_id=id, user_id_id=uid )
    data.save()

    return redirect('/user/cart/1')



def cart(request,id):

    cart = UserCartModel.objects.filter(user_if_id=id)
    item = ProductModel.objects.all()
    return render(request,'user/cart.html',{'cart':cart,'item':item})


def delete_cart(request,id,uid):
        data = UserCartModel.objects.filter(product_id_id=id,user_if_id=uid)
        data.delete()

        cart = UserCartModel.objects.filter(user_if_id=id)
        item = ProductModel.objects.all()
        return redirect('/user/cart/1')



