from .views import BlogPostView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.urls import path

urlpatterns = [
    path("", BlogPostView.as_view(), name="blog"),
    path("post/new", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("post/<int:pk>/delete" , BlogDeleteView.as_view(), name='blog_delete')
]
