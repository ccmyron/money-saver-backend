# money_saver/urls.py

from django.contrib import admin
from django.urls import path, include

# from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('store.urls')),
    path('', include('myapi.urls')),
]
