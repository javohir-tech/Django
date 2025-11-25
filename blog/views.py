from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

class BlogPostView(ListView) :
    model = BlogPost ;
    template_name = 'blog.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['object_list']
        return context
    
class BlogDetailView(DetailView) :
    model = BlogPost;
    template_name = 'blog_detail.html'
    
# Create your views here.
