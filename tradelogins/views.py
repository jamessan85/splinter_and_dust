# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView
from django.template.context_processors import csrf
from tradelogins.forms import UserRegistrationForm, UserLoginForm, AccountInformation
from .models import User, AccountInfo
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))
            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request)),

    return render(request, 'traderegister.html', args)

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



