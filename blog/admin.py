from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/Date', {'fields': ['title', 'date_posted']}),
        ('Content', {'fields': ['content']}),
        ('Author', {'fields': ['author']}),
    ]



admin.site.register(Post, PostAdmin)