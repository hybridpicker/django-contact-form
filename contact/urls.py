from django.contrib import admin
from django.urls import path, include
from form import views

urlpatterns = [
    path('', include('form.urls')),
]
