"""shopbilling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.shortcuts import render

urlpatterns = [
    path("",lambda request:render(request,"bill/admin.html")),
    path('order', ordercreate.as_view(), name='order'),
    path('orderlines/<str:bill_number>', orderlines.as_view(), name='orderlines'),
    path('product', productcreate.as_view(), name='product'),
    path('purchase', purchsecreate.as_view(), name='purchase'),
    path('generate/<str:bill_number>', billgenerate.as_view(), name='generate'),
    path('adminpage', adminpagecontent.as_view(), name='admin')
]
