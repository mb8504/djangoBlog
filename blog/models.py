from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

class PostCategory(models.Model):
    category = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    path = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='image')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(PostCategory, default=1, on_delete=models.SET_DEFAULT)
    path = models.CharField(max_length=200, default=1)

    def save(self, *args, **kwargs):
        self.path = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title