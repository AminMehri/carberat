from django.db import models
from Utils.models import BaseBlog
from ckeditor.fields import RichTextField


class Category(BaseBlog):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.CASCADE, related_name="children")
    thumbnail =  models.ImageField(upload_to='media/category')

    class Meta:
        ordering = ['-parent__id']



class Article(BaseBlog):
    category = models.ManyToManyField(Category)
    thumbnail =  models.ImageField(upload_to='media/article')
    main_page_show = models.BooleanField(default=True)

    class Meta:
        ordering = ['-updated']



class ContactUs(models.Model):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=512, )
    content = RichTextField()
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.subject