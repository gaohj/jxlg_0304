from django.shortcuts import render
from .models import Book,Author,Publisher,BookOrder
from django.db.models import Avg,Count,Max,Min,F,Q,Sum
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


def index6(request):
    #查看作者的最大年龄 和最小年龄
    #select username as 用户名
    result = Author.objects.aggregate(max=Max("age"),min=Min("age"))
    print(result)
    print(connection.queries[-1])

    #每一本书 售卖的时候 最大价格 和最小价格
    books = Book.objects.annotate(max=Max("bookorder__price"),min=Min("bookorder__price"))
    for book in books:
        print("%s:%s:%s" % (book.name,book.max,book.min))
    return HttpResponse("最大年龄和最小年龄")

def index7(request):
    #1.所有图书的销售总额
    result = BookOrder.objects.aggregate(total=Sum("price"))
    print(result)
    print(connection.queries[-1])
    print("@"*50)
    #2.每一本图书的销售总额
    books = Book.objects.annotate(total=Sum("bookorder__price"))
    for book in books:
        print("%s:%s" % (book.name,book.total))
    print(connection.queries[-1])
    print("@" * 50)
    #2018年度的销售总额
    result = BookOrder.objects.filter(create_time__year=2018).aggregate(total=Sum("price"))
    print(result)
    print(connection.queries[-1])
    print("@" * 50)
    #每一本书在2018年度的销售总额
    books = Book.objects.filter(bookorder__create_time__year=2018).annotate(total=Sum("bookorder__price"))
    for book in books:
        print("%s:%s" % (book.name, book.total))
    print(connection.queries[-1])
    print("@" * 50)
    return HttpResponse("销售总额")

def index8(request):
    #给每一本书的售价增加10元钱
    # books = Book.objects.all()
    # for book in  books:
    #     book.price += 10
    #     book.save()
    Book.objects.update(price=F("price")+10)
    print(connection.queries[-1])
    return HttpResponse("保存成功")

def index9(request):
    #价格100块钱以上  评分4.9分以上
    #books = Book.objects.filter(price__gte=100,rating__gte=4.9)
    #books = Book.objects.filter(Q(price__gte=100)&Q(rating__gte=4.9))
    #books = Book.objects.filter(Q(price__gte=100)|Q(rating__gte=4.9))
    books = Book.objects.filter(Q(price__gte=100)&~Q(name__icontains="传"))
    for book in books:
        print("%s:%s" % (book.name,book.rating))
    print(connection.queries[-1])
    return HttpResponse("Q表达式")