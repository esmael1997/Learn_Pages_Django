from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm
from django.views import View 
from django.views.generic.edit import FormView

class Blog(LoginRequiredMixin,ListView):
    
    template_name = "blog.html" 
    model = Post
    context_object_name = "posts"
    
    
class BlogDetailView(LoginRequiredMixin,DetailView):
    
    model = Post
    template_name = "post_detail.html"
    context_object_name = 'post'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post=self.object)
        return context
    
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            
            return redirect('post_detail', pk=self.object.pk)
        
        context = self.get_context_data(form=form)
        
        return self.render_to_response(context)
    
    
class BlogCreateView(LoginRequiredMixin,CreateView):  
    model = Post
    template_name = "post_new.html"
    fields = ["title", "body"]
    success_url = reverse_lazy('blog')
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): 
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"] 
       
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): 
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    
class Commentget(DetailView):
    model = Post
    template_name = "post_detail.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context  
    
class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "post_detail.html"
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        post = self.get_object()
        return reverse_lazy('post_detail', kwargs={'pk': post.pk})
    