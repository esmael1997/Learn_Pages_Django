from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Post(models.Model):
    body = models.TextField()
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False, blank=False
        )
    
    title = models.CharField(max_length=255, default=" ")
    
    def __str__(self):
        return self.title[:20]
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    comment = models.CharField(max_length=255)
    
    author = models.ForeignKey(
        #User,
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,

    )
    #body = models.TextField()
    #created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
    #def get_absolute_url(self):
        #return reverse("post_detail")