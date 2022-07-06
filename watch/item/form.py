from pyexpat import model
from django import forms
from item.models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields ="__all__"