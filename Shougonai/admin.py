from django.contrib import admin
from django.contrib.auth.admin import UserAdmin



# Register your models here.
from .models import Posts, Comment

class CommentInline(admin.TabularInline):
    model = Comment

class PostsAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]





admin.site.register(Posts, PostsAdmin)
admin.site.register(Comment)
