from django.contrib import admin
from .models import Post, PostCategory
from django.db import models 

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/Date', {'fields': ['title', 'date_posted']}),
        ('Image', {'fields': ['image']}),
        ('Content', {'fields': ['content']}),
        ('Author', {'fields': ['author']}),
        ('URL', {'fields': ['path']}),
        ('Categories', {'fields': ['category']}),

    ]

admin.site.register(PostCategory)


admin.site.register(Post, PostAdmin)
