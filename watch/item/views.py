import imp
from django.shortcuts import redirect, render
from item.models import ProductModel
from item.form import ProductForm

# Create your views here.


def add(request):
    data = ProductForm(request.POST, request.FILES)
    data.save()

    return redirect('/admin/item') 

def edit(request,id):
    data = ProductModel.objects.get(id=id)

    return redirect('/admin/additem',{'product':data}) 

def delete(request,id):
    data = ProductModel.objects.get(id=id)
    data.delete()
    return redirect('/admin/item') 

def update(request,id):
    data = ProductModel.objects.get(id=id)
    form = ProductForm(request.POST,request.Files,instance=data)

    form.save()

    return redirect('/admin/item') 

def details(request,id):
    data = ProductModel.objects.get(id=id)

    return render(request,'user/details.html',{'data':data})
