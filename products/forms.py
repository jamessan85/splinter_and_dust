from django import forms
from .models import Product, Collection

class EnterProductsForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'price', 'product_info', 'image', 'range')

