from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('index.html', views.homepage, name='homepage'),
    path('product-detail.html/', views.productDetail, name='productDetail'),
    path('about.html', views.aboutPage, name='about'),
    path('contact.html', views.contactPage, name='contact'),
    path('parsejson/', views.parsejson, name='scripttrigger'),
]
