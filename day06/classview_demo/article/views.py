from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.

class ArticleListView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'article_list.html')
    def post(self,request,*args,**kwargs):
        return HttpResponse("post")