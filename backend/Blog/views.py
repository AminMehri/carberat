from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from jalali_date import datetime2jalali
from Blog.models import Article, Category



class ShowArticles(APIView):

    def get(self, request):
        slug = self.request.query_params.get('slug')
        if slug:
            articles = Article.objects.published().filter(category__slug=slug).order_by('-date')
        else:
            articles = Article.objects.published().order_by('-date')
        data = []
        for article in articles:
            data.append({
                'id': article.id,
                'title': article.title,
                'slug': article.slug,
                'category': [a.title for a in article.category.published()],
                'description': article.description,
                'thumbnail': article.thumbnail.url,
                'date': datetime2jalali(article.date).strftime('14%y/%m/%d _ %H:%M'),
            })
        return Response(data, status=status.HTTP_200_OK)



class ShowSpecificArticles(APIView):

    def get(self, request):
        slug = self.request.query_params.get('slug')
        articles = Article.objects.published().filter(category__slug=slug).order_by('-date')
        data = []
        for article in articles:
            data.append({
                'id': article.id,
                'title': article.title,
                'slug': article.slug,
                'category': [a.title for a in article.category.published()],
                'description': article.description,
                'thumbnail': article.thumbnail.url,
                'date': datetime2jalali(article.date).strftime('14%y/%m/%d _ %H:%M'),
            })
        return Response(data, status=status.HTTP_200_OK)


class ShowSingleArticle(APIView):

    def get(self, request):
        slug = self.request.query_params.get('slug')
        if not Article.objects.published().filter(slug=slug).exists():
            return Response({"message": "Article is not find"}, status=status.HTTP_404_NOT_FOUND)
        article = Article.objects.published().get(slug=slug)
        data = [{
            'title': article.title,
            'content': article.content,
            'category': [[a.title, a.slug] for a in article.category.published()],
            'date': datetime2jalali(article.date).strftime('14%y/%m/%d _ %H:%M'),
        }]
        return Response(data, status=status.HTTP_200_OK)



class ShowCategories(APIView):

    def get(self, request):
        categories = Category.objects.published().order_by('-date')
        data = []
        for category in categories:
            data.append({
                'id': category.id,
                'title': category.title,
                'slug': category.slug,
                'parent': category.parent.title if category.parent else None,
                'children': [[a.title, a.slug] for a in category.children.all()],
                'description': category.description,
                'thumbnail': category.thumbnail.url,
                'date': datetime2jalali(category.date).strftime('14%y/%m/%d _ %H:%M'),
            })
        return Response(data, status=status.HTTP_200_OK)



class ShowSingleCategory(APIView):

    def get(self, request):
        slug = self.request.query_params.get('slug')
        if not Category.objects.published().filter(slug=slug).exists():
            return Response({"message": "Category is not find"}, status=status.HTTP_404_NOT_FOUND)
        category = Category.objects.published().get(slug=slug)
        data = [{
            'title': category.title,
            'content': category.content,
            'parent': category.parent.title if category.parent else None,
            'date': datetime2jalali(category.date).strftime('14%y/%m/%d _ %H:%M'),
        }]
        return Response(data, status=status.HTTP_200_OK)