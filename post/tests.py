from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="blog for start work")
        
    def test_model_content(self):
        self.assertEqual(self.post.text, "blog for start work")
        
    def test_url_exists_at_correct_location(self):  
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("blog"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self):  
        response = self.client.get(reverse("blog"))
        self.assertTemplateUsed(response, "blog.html")

    def test_template_content(self):  
        response = self.client.get(reverse("blog"))
        self.assertContains(response, "blog for start work")
        
