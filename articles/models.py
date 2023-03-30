from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(auto_now_add=False, auto_now=False, 
                                   null=True, blank=True)