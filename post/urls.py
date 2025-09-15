from django.urls import path
from .views import Blog


urlpatterns = [
    path('', Blog.as_view(), name="blog"),
    
]