from django.contrib import admin
from django.urls import path, include
from Blog import views

urlpatterns = [
    path('articles/', views.ShowArticles.as_view()),
    path('specific-articles/', views.ShowSpecificArticles.as_view()),
    path('article/', views.ShowSingleArticle.as_view()),
    path('categories/', views.ShowCategories.as_view()),
    path('category/', views.ShowSingleCategory.as_view()),
    path('contact/', views.Contact.as_view()),
]
