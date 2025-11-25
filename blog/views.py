from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
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
    def get_context_data(self , **kwargs) :
        context = super().get_context_data(**kwargs);
        context['post'] = context['object']
        return context
    
class BlogCreateView(CreateView) :
    model = BlogPost
    template_name = 'post_new.html'
    fields = ['title' , 'text' , 'author']
    
class BlogUpdateView(UpdateView) :
    model = BlogPost 
    template_name = 'post_edit.html'
    fields = ['title' , 'text']

    
# Create your views here.
