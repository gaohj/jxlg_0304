from django.shortcuts import render
from datetime import datetime

def greet(word):
    return "hello world %s" % word


def index(request):
    context = {
        'greet':greet
    }
    return render(request,'index.html',context=context)

def add_view(request):
    context = {
        "v1":['1','a','3'],
        "v2":['4','b','6']
    }
    return render(request, 'add.html', context=context)

def cut_view(request):
    return render(request, 'cut.html')

def date_view(request):
    context = {
        'today':datetime(year=2019,month=6,day=13,hour=15,minute=10,second=10)
    }
    return render(request, 'date.html',context=context)

