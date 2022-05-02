from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('homeN/',views.homeNationalize,name='homeN'),
]