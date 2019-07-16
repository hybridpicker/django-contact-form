from django.contrib import admin
from django.urls import path
from form import views

urlpatterns = [
    path('contact/', views.emailView, name='contact_email'),
    path('contact/success/', views.successView, name='success_contact'),
]
