from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Article
from .forms import ArticleForm
# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request,'index.html')
    # def post(self,request):
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     file = request.FILES.get('thumbnail')
    #     Article.objects.create(title=title,content=content,thumbnail=file)
    #     return HttpResponse("成功")
    def post(self,request):
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("ok")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("fail")