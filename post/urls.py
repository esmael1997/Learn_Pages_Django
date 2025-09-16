from django.urls import path
from .views import Blog, BlogDetailView


urlpatterns = [
    path('', Blog.as_view(), name="blog"),
    path('/<int:pk>/', BlogDetailView.as_view(), name="post_detail"),
]