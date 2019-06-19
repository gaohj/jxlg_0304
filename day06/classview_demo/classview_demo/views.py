#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render,reverse,redirect
from django.views.generic import View,TemplateView
from django.views.decorators.http import require_http_methods,require_POST,require_GET

@require_GET
def index(request):
    return HttpResponse("首页")

class BookListView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("book list view")

class AddBookView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'add_book.html')
    def post(self,request,*args,**kwargs):
        book_name = request.POST.get('name')
        book_author = request.POST.get('author')
        print("name:{},author:{}".format(book_name,book_author))
        return HttpResponse("添加成功")
    def put(self,request,*args,**kwargs):
        return HttpResponse("更新")
    def delete(self,request,*args,**kwargs):
        return HttpResponse("删除")

class BookDetailView(View):
    def get(self,request,book_id):
        print("图书的id是:%s" % book_id)
        return HttpResponse("图书详情")
    
    def dispatch(self, request, *args, **kwargs):
        print("任何请求都会走这里")
        return super(BookDetailView, self).dispatch(request, *args, **kwargs)
    
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("不支持GET外的其它请求")


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = {
            "phone":"400-811-9990"
        }

        return context

