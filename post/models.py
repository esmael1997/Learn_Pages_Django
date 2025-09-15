from django.db import models
from django.urls import reverse

class Post(models.Model):
    text = models.TextField()
    auther = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=255, default=" ")
    
    def __str__(self):
        return self.title[:20]
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    