# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView
from django.template.context_processors import csrf
from django.template.loader import render_to_string
from tradelogins.forms import TradeRegistrationForm, UserLoginForm, AccountInformation, CustRegistrationForm
from .models import User, AccountInfo
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
import stripe
import arrow
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

def register(request):
    if request.method == 'POST':
        form = TradeRegistrationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=999,
                    currency="GBP",
                    description=form.cleaned_data['email'],
                    card=form.cleaned_data['stripe_id'],
                )

                if customer:
                    user = form.save()
                    user.stripe_id = customer.id
                    user.subscription_end = arrow.now().replace(weeks=+4).datetime
                    user.user_type = 'T'
                    user.save()

                if customer.paid:

                    user = auth.authenticate(email=request.POST.get('email'),
                                             password=request.POST.get('password1'))
                    if user:
                        auth.login(request, user)

                        messages.success(request, "You have successfully registered")
                        return redirect(reverse('profile'))
                    else:
                        messages.error(request, "unable to log you in at this time!")
                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")
    else:
        today = datetime.date.today()
        form = TradeRegistrationForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'traderegister.html', args)


def registercust(request):
    if request.method == 'POST':
        form = CustRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = CustRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'custregister.html', args)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('home'))

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/login/')
def accountinformation(request):
        if request.method == "POST":
            form = AccountInformation(request.POST, request.FILES)
            if form.is_valid():
                accountinfo = form.save(commit=False)
                accountinfo.account_id = request.user.id
                accountinfo.save()
                return redirect(profile)
        else:
            form = AccountInformation()
        return render(request, 'userinformation.html', {'form': form})

@login_required
def editaccountinfo(request, account_num):

    account = get_object_or_404(AccountInfo, pk=account_num)

    if request.method == "POST":
        form = AccountInformation(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AccountInformation(instance=account)

    args = {
        'form': form,
        'form_action': reverse('editaccountinfo', kwargs={'account_num': account.id}),
    }
    args.update(csrf(request))

    return render(request, 'userinformation.html', args)

@login_required(login_url='/login/')
def cancel_subscription(request):
    try:
        customer = stripe.Customer.retrieve(request.user.stripe_id)
        customer.cancel_subscription(at_period_end=True)
    except Exception, e:
        messages.error(request, e)
    return redirect('home')



