from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class Blog(ListView):
    
    template_name = "blog.html" 
    
    model = Post

