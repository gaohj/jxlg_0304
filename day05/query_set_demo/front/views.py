from django.shortcuts import render
from .models import Book,Author,Publisher,BookOrder
from django.db.models import Avg,Count,Max,Min,F,Q
from django.http import HttpResponse
from django.db import connection
# Create your views here.
def index(request):
    print(type(Book.objects))
    return HttpResponse("首页")

def index2(request):
    #链式调用
    books = Book.objects.filter(id__gte=1).exclude(id=3)
    for book in  books:
        print(book)
    return HttpResponse("链式调用")

def index3(request):
    #获取所有图书的定价的平均价
    book = Book.objects.aggregate(avg=Avg("price"))
    print(book)
    print(connection.queries)
    return HttpResponse("首页")

def index4(request):
    #获取每一本图书销售的平均价格
    #主要的表为图书表  条件是图书订单表中的
    #图书订单表模型的小写__字段
    # result = Book.objects.aggregate(avg=Avg("bookorder__price"))
    # print(result)
    # print(connection.queries)
    print("="*50)
    result = Book.objects.annotate(avg=Avg("bookorder__price"))
    for res in result:
        print("%s/%s" %(res.name,res.avg))
    return HttpResponse("每一本图书销售的平均价格")

def index5(request):
    #获取book表中总共有多少本书
    result = Book.objects.aggregate(book_nums=Count("id"))
    print(result)
    print(connection.queries)

    #作者表中总共有多少个不同的邮箱
    result = Author.objects.aggregate(email_nums=Count("email",distinct=True))
    print(result)
    print(connection.queries)

    #统计每一本书的销量
    books = Book.objects.annotate(book_nums=Count("bookorder"))
    for book in books:
        print("%s:%s" % (book.name,book.book_nums))
    return HttpResponse("book表中总共有多少本书")
