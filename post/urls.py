from django.urls import path
from .views import Blog, BlogDetailView, BlogCreateView, BlogUpdateView , BlogDeleteView



urlpatterns = [
    path('', Blog.as_view(), name="blog"),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new/', BlogCreateView.as_view(), name='post_new'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name="post_edit"),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name="post_delete"),
]