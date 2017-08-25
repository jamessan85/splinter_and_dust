# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Product, Collection
from .forms import EnterProductsForm, ProductPurchaseForm
from tradelogins.models import AccountInfo, Purchase
from django.contrib import messages, auth
from django.views.generic.list import ListView
from django.contrib import admin
from django.conf import settings
import datetime
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

#show product by collection
def sort_by_collection(request, collection):
    product = Product.objects.filter(range=collection)
    return render(request, 'collections.html', {'product':product})

#show page for all company names
def show_companies(request):
    accountinfo = AccountInfo.objects.all()
    return render(request, 'companyhome.html', {'accountinfo': accountinfo})

# pass two models into one view to filter on both views
def sort_by_company(request, company):
    product = Product.objects.filter(userid=company)
    banner = AccountInfo.objects.filter(account_id=company)
    ctx = {'banner':banner, 'product':product}
    return render(request, 'companies.html', ctx)

#displays all products
def product_display(request):
    product = Product.objects.all()
    return render(request, 'home.html', {'product': product})

#display information regarding each product when selected.
def product_detail(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/productinfo.html", {'product': product})

#generates view for entering a new product form
def new_product(request):
    if request.method == "POST":
        form = EnterProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.creator = request.user #saves user to product.creator model
            product.userid = request.user.id #saves user.id to product.userid model
            product.save()
            return redirect(new_product)
    else:
        form = EnterProductsForm()
    return render(request, 'enternewproduct.html', {'form': form})

#view all products created by that account
def products_by_user(request):
    product = Product.objects.all
    return render(request, 'userproducts.html', {'product': product})

#edit a product
@login_required
def edit_product(request, edit_prod):

    product = get_object_or_404(Product, pk=edit_prod)

    if request.method == "POST":
        form = EnterProductsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('productsbyuser')
    else:
        form = EnterProductsForm(instance=product)

    args = {
        'form': form,
        'form_action': reverse('editproduct', kwargs={'edit_prod': product.id}),
    }
    args.update(csrf(request))

    return render(request, 'enternewproduct.html', args)

#purchase a product, generates form
@login_required(login_url='/login/')
def purchase(request, purchase):

    product = get_object_or_404(Product,pk=purchase)

    if request.method == 'POST':
        form = ProductPurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user_id = request.user.id
            purchase.product_id = product.id
            purchase.title = product.title
            purchase.product_info = product.product_info
            purchase.price = product.price
            purchase.save()
            try:
                customer = stripe.Charge.create(
                    amount=int(product.price * 100),
                    currency="GBP",
                    description=product.title,
                    card=form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    form.save()
                    return redirect(reverse('profile'))
                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")
    else:
        today = datetime.date.today()
        form = ProductPurchaseForm()

    args = {'form': form,
            'publishable': settings.STRIPE_PUBLISHABLE,
            'product': product,
            }
    args.update(csrf(request))

    return render(request, 'products/purchase.html', args)

#view to see the products the user has bought
def products_bought(request, userid):
    product = Product.objects.filter(userid=userid)
    purchase = Purchase.objects.filter(user_id=userid)
    ctx = {'purchase':purchase, 'product':product}
    return render(request, 'products/productsbought.html', ctx)