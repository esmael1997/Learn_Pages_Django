from django.contrib import admin
from .models import Post
from .models import Comment

class CommentInline(admin.TabularInline):
    model = Comment
    #extra = 1
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]   

admin.site.register(Comment)

admin.site.register(Post, PostAdmin)
# Register your models here.
