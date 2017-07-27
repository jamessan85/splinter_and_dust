"""splinter_an_dust URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from products import views as products_views
from tradelogins import views as tradelogin_views
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', products_views.product_display, name='home'),
    url(r'^home/collection/(?P<collection>\w+)/$', products_views.sort_by_collection, name='collection'),
    url(r'^home/company/$', products_views.show_companies, name='companiesall'),
    url(r'^home/company/(?P<company>\d+)/$', products_views.sort_by_company, name='companies'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^media/banners/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^media/logo_square/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^home/products/(?P<id>\d+)/$', products_views.product_detail, name='productbyid'),
    url(r'^home/products/$', products_views.products_by_user, name='productsbyuser'),
    url(r'^home/products/purchase/(?P<purchase>\d+)/$', products_views.purchase, name='purchase'),
    url(r'^home/products/edit/(?P<edit_prod>\d+)/$', products_views.edit_product, name='editproduct'),
    url(r'^register/$', tradelogin_views.register, name='register'),
    url(r'^register/cust/$', tradelogin_views.registercust, name='custregister'),
    url(r'^profile/$', tradelogin_views.profile, name='profile'),
    url(r'^profile/productsbought/(?P<userid>\d+)/$', products_views.products_bought, name='prodbought'),
    url(r'^product/new/$', products_views.new_product, name='new_product'),
    url(r'^login/$', tradelogin_views.login, name='login'),
    url(r'^logout/$', tradelogin_views.logout, name='logout'),
    url(r'^profile/accountinfo/$', tradelogin_views.accountinformation, name='accountinformation'),
    url(r'^profile/accountinfo/edit/(?P<account_num>\d+)/$', tradelogin_views.editaccountinfo, name='editaccountinfo'),
]
