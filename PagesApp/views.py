from django.shortcuts import render
from django.views.generic import ListView
from .models import POST

class HomePageView(ListView) :
    model = POST;
    template_name = "home.html"