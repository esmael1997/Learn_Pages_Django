from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class Blog(ListView):
    
    template_name = "blog.html" 
    
    model = Post

class BlogDetailView(DetailView):
    
    model = Post
    
    template_name = "post_detail.html"
    
    context_object_name = 'posts'