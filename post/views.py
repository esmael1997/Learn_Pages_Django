from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

class Blog(ListView):
    
    template_name = "blog.html" 
    model = Post

class BlogDetailView(DetailView):
    
    model = Post
    template_name = "post_detail.html"
    context_object_name = 'post'
    
class BlogCreateView(CreateView):  
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]