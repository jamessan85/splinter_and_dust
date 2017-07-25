# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Product, Collection
from .forms import EnterProductsForm
from tradelogins.models import AccountInfo
from django.views.generic.list import ListView
from django.contrib import admin
# Create your views here.


def sort_by_collection(request, collection):
    product = Product.objects.filter(range=collection)
    return render(request, 'collections.html', {'product':product})


#### pass two models into one view to filter
def sort_by_company(request, company):
    product = Product.objects.filter(userid=company)
    banner = AccountInfo.objects.filter(account_id=company)
    ctx = {'banner':banner, 'product':product}
    return render(request, 'companies.html', ctx)

def product_display(request):
    product = Product.objects.all()
    return render(request, 'home.html', {'product': product})

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

def new_product(request):
    if request.method == "POST":
        form = EnterProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.creator = request.user
            product.userid = request.user.id
            product.save()
            return redirect(new_product)
    else:
        form = EnterProductsForm()
    return render(request, 'enternewproduct.html', {'form': form})

def products_by_user(request):
    product = Product.objects.all
    return render(request, 'userproducts.html', {'product': product})

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

# class UserProducts(ListView):
#         userid = 7
#         queryset = Product.objects.filter(userid__exact=userid)
#         template_name = 'products/product_list.html'
