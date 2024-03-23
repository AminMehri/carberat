from django.contrib import admin
from Blog.models import Article, Category, ContactUs



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_category', 'date', 'status')
    search_fields = ['title', 'slug']

    def get_category(self, obj):
        return " ,".join([p.title for p in obj.category.all()])
    get_category.short_description = "categories"



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent','date', 'status')
    search_fields = ['title', 'slug']


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'seen')
    search_fields = ['full_name', 'subject']
