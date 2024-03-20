from django.db import models
from Utils.models import BaseBlog



class Category(BaseBlog):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.CASCADE, related_name="children")
    thumbnail =  models.ImageField(upload_to='media/category')

    class Meta:
        ordering = ['parent__id']



class Article(BaseBlog):
    category = models.ManyToManyField(Category)
    thumbnail =  models.ImageField(upload_to='media/article')
