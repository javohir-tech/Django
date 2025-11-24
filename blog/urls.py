from .views import BlogPostView
from django.urls import path

urlpatterns = [
    path('' , BlogPostView.as_view(), name = 'blog')
]

