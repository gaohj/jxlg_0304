from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category
from datetime import datetime,time
from django.utils.timezone import make_aware

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
    # aricles = Article.objects.filter(id__lte=2)
    # aricles = Article.objects.filter(id__lt=2)
    # aricles = Article.objects.filter(id__gt=2)
    aricles = Article.objects.filter(id__gte=2)
    print(aricles.query)
    print(aricles)
    return HttpResponse("index4")

def index5(request):
    start_time = make_aware(datetime(year=2018,month=12,day=13,hour=11,minute=13,second=14))
    end_time = make_aware(datetime(year=2019,month=12,day=13,hour=11,minute=13,second=14))
    articles = Article.objects.filter(create_time__range=(start_time,end_time))
    print(articles.query)
    for article in articles:
        print(article)
    return HttpResponse("index5")

def index5(request):
    start_time = time(hour=11, minute=13, second=14)
    end_time = time(hour=21, minute=13, second=14)
    # articles = Article.objects.filter(create_time__date=datetime(year=2018,month=6,day=6))
    # articles = Article.objects.filter(create_time__year__gte=2018)
    # articles = Article.objects.filter(create_time__week_day=4)
    articles = Article.objects.filter(create_time__time__range=(start_time,end_time))
    print(articles.query)
    for article in articles:
        print(article)
    return HttpResponse("index5")

def index6(request):
    # aricles = Article.objects.filter(create_time__isnull=False)
    aricles = Article.objects.filter(title__iregex=r"^hello")
    print(aricles.query)
    for aricle in aricles:
        print(aricle)
    return HttpResponse("index6")

def index7(request):
    categories = Category.objects.filter(articles__title__contains="hello")
    print(categories.query)
    print(categories)
    return HttpResponse("index7")
