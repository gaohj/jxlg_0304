from django.shortcuts import render,redirect,reverse
from django.db import connection

def get_cursor():
    return connection.cursor()
# Create your views here.

def index(request):
    cursor = get_cursor()
    cursor.execute("select id,name,author,price from book")
    books = cursor.fetchall()
    return render(request,'index.html',context={"books":books})

def add_book(request):
    if request.method == "GET":
        return render(request,'add_book.html')
    else:
        name = request.POST.get('name')
        author = request.POST.get('author')
        price = float(request.POST.get('price'))
        cursor = get_cursor()
        cursor.execute("insert into book(id,name,author,price) values(null,'%s','%s',%d)" % (name,author,price))
        return redirect(reverse('index'))
def book_detail(request,book_id):
    cursor = get_cursor()
    cursor.execute("select id,name,author,price from book where id=%s" % book_id)
    book = cursor.fetchone()
    return render(request,'book_detail.html',context={"book":book})

def delete_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        cursor = get_cursor()
        cursor.execute("delete from book where id=%s" % book_id)
        return redirect(reverse('index'))
    else:
        raise RuntimeError('删除图书的方法不被允许')