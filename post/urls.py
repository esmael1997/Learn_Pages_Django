from django.urls import path
from .views import Blog, BlogDetailView, BlogCreateView, BlogUpdateView



urlpatterns = [
    path('', Blog.as_view(), name="blog"),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new/', BlogCreateView.as_view(), name='blog_new'),
    path('edit/', BlogUpdateView.as_view(), name="post_edit"),
]