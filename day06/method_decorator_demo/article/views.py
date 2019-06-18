from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.decorators.http import require_http_methods,require_GET,require_POST,require_safe



# Create your views here.
# @require_http_methods(['GET'])
#@require_GET  = @require_http_methods(['GET'])
#@require_http_methods(['POST'])  = require_POST
@require_GET
def index(request):
    articles = Article.objects.all()

    return render(request,'index.html',context={"articles":articles})
@require_http_methods(['GET','POST'])
def add_article(request):
    if request.method == 'GET':
        return render(request,'add_article.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        price = request.POST.get('price')
        Article.objects.create(title=title,content=content,price=price)
        return HttpResponse("成功")

# 增  insert   POST
#删   delete   DELETE
#改   update    PUT PATCH
#查   select    GET