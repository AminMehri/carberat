from django.db import models
from ckeditor.fields import RichTextField



class BlogManager(models.Manager):
    def published(self):
        return self.filter(status='p')



class BaseBlog(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish'),
    )
    title = models.CharField(max_length=128)
    eng_title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    content = RichTextField()
    key_words = models.CharField(max_length=1024)
    meta_title = models.CharField(max_length=256)
    meta_description = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    objects = BlogManager()

    class Meta:
        abstract=True
        
    def __str__(self):
        return self.title