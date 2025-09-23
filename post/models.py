from django.db import models
from django.urls import reverse
from django.conf import settings


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
    
    