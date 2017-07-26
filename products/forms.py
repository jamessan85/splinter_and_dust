from django import forms
from .models import Product, Collection
from tradelogins.models import *

class EnterProductsForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'price', 'product_info', 'image', 'range')

class ProductPurchaseForm(forms.ModelForm):
    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in xrange(2015, 2036)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Purchase
        fields = ['stripe_id']
