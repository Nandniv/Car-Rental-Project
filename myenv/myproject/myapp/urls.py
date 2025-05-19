"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from . import views 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('index/', views.index, name='index'),
    path('lindex/', views.lindex, name='lindex'),
    path('signup/', views.signup, name='signup'),
    path('add/', views.add, name='add'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cpass/', views.cpass, name='cpass'),
    path('view/', views.view, name='view'),
    path('fpass/', views.fpass, name='fpass'),
    path('otp/', views.otp, name='otp'),
    path('newpass/', views.newpass, name='newpass'),
    path('uprofile/',views.uprofile,name='uprofile'),
    path('update/<int:pk>',views.update,name='update'),
    path('details/<int:pk>',views.details,name='details'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('uprofilelessor/',views.uprofilelessor,name='uprofilelessor'),
    path('car/',views.car,name='car'),
    path('car/carsingle/', views.carsingle, name='carsingle'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('cart/<int:pk>/', views.cart, name='cart'),
    path('summary/<int:pk>/', views.summary, name='summary'),
    path('success/',views.success,name='success'),
    path('index/services.html/',views.services,name='services'),
    path('index/about.html/', views.about, name='about'),
    path('index/labout.html/', views.labout, name='labout'),
    path('send-otp/', views.send_otp_view, name='send_otp'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),


    path('car/<int:pk>/', views.details, name='details'),
    path('myorder/', views.myorder, name='myorder'),
    path('cancelorder/<int:booking_id>/', views.cancelorder, name='cancelorder'),
    path('pay/<int:booking_id>/', views.pay, name='pay'),
    path('invoice/<int:pk>/', views.generate_invoice_pdf, name='generate_invoice_pdf'),
    path('pricing/', views.pricing, name='car:pricing'),
    



]
