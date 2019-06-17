from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category
from datetime import datetime

# Create your views here.
def index(request):
    # aricle = Article.objects.filter(title__iexact="hello world")
    aricle = Article.objects.filter(title__exact="hello world")
    print(type(aricle))
    print(aricle.query)
    print(aricle)
    return HttpResponse("index")

def index1(request):
    article = Article.objects.get(pk=1)
    print(type(article))
    # print(article.query)
    return HttpResponse("index1")

#query 用来查看 orm最终执行的sql语句  但是query 只能被用在queryset 对象上 也就是 filter 条件
# objects.get() 这种情况下不能用 。query 去查看最终翻译的sql 语句

def index2(request):
    #article = Article.objects.filter(title__contains='谷')
    article = Article.objects.filter(title__icontains='谷')
    #print(type(article))
    print(article.query)
    print(article)
    return HttpResponse("index2")

def index3(request):
    # articles = Article.objects.filter(id__in=[1,4])
    # print(articles.query)
    # for article in articles:
    #     print(article)
    # categories = Category.objects.filter(articles__in=[1,4])
    # print(categories.query)
    # for category in categories:
    #     print(category)
    #标题中包含 hello的分类
    articles = Article.objects.filter(title__contains='hello')
    categories = Category.objects.filter(articles__in=articles)
    for category in categories:
        print(category)
    return HttpResponse("index3")

def index4(request):
    aricles = Article.objects.filter(id__gte=2)
    print(aricles.query)
    print(aricles)
    return HttpResponse("index4")

