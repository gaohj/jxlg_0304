from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,User
from .forms import AddBookForm

# Create your views here.

def add_book(request):
    form = AddBookForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        page = form.cleaned_data.get('page')
        price = form.cleaned_data.get('price')
        print("title:%s" % title)
        print("title:%s" % page)
        print("title:%s" % price)
        return HttpResponse("success")
    else:
        print(form.get_errors())
        return HttpResponse("false")