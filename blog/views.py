from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

class BlogPostView(ListView) :
    model = BlogPost ;
    template_name = 'blog.html'
    
class BlogDetailView(DetailView) :
    model = BlogPost;
    template_name = 'blog_detail.html'
    
# Create your views here.
