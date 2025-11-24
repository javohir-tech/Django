from .views import BlogPostView, BlogDetailView
from django.urls import path

urlpatterns = [
    path('', BlogPostView.as_view(), name='blog'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
