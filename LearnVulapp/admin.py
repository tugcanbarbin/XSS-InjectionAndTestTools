from django.contrib import admin

# Register your models here.
from .models import Book, Comment,Post
admin.site.register(Book)
admin.site.register(Post)
admin.site.register(Comment)