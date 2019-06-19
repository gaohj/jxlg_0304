from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# Create your views here.

def view_403(request):
    return render(request,'errors/403.html',status=403)

def view_405(request):
    return render(request,'errors/405.html',status=405)
