"""myfirstsite URL Configuration

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'), #http://127.0.0.1:8000/data/reg
    path('login/', views.login, name='login'),
    path('cartdata/', views.cart,name='cartdata'),
    path('cartdat/', views.cartwomen,name='cartdatawomen'),
    path('cartcontent/', views.cartcontent,name='cartcontent'),
    path('ordernow/', views.order,name="order"),
    path('mendata/', views.productmen,name="productmen"),
    path('meninfo/', views.mendetails,name="mendetails"),
    path('womendata/', views.productwomen,name="productwomen"),
    path('womeninfo/', views.womendetails,name="womendetails"),
    path('profile/', views.profiledetails,name="profiledetails"),

]
