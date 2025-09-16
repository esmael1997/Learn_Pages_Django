from django.urls import path
from .views import Blog, BlogDetailView, BlogCreateView



urlpatterns = [
    path('', Blog.as_view(), name="blog"),
    
    
]