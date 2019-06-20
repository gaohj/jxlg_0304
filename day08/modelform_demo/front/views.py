from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,User
from .forms import AddBookForm,RegisterForm
from django.views.decorators.http import require_POST

# Create your views here.

def add_book(request):
    form = AddBookForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        page = form.cleaned_data.get('page')
        price = form.cleaned_data.get('price')
        # print("title:%s" % title)
        # print("title:%s" % page)
        # print("title:%s" % price)
        form.save()
        return HttpResponse("success")
    else:
        print(form.get_errors())
        return HttpResponse("false")
@require_POST
def register(request):
    forms = RegisterForm(request.POST)
    if forms.is_valid():
        #commit 表示 username和telephone 添加到数据库中 但是 并没有提交
        user = forms.save(commit=False)
        user.password = forms.cleaned_data.get('pwd1')
        user.save()
        return HttpResponse("成功")
    else:
        print(forms.errors.get_json_data())
        return HttpResponse("失败")
