from django.shortcuts import render
from django.views.generic import View
from .forms import MessageBoardForm,RegisterForm
from django.http import HttpResponse
from .models import User

# Create your views here.

class IndexView(View):
    def get(self,request,*args,**kwargs):
        form = MessageBoardForm()
        return render(request,'index.html',context={"form":form})
    def post(self,request):
        form = MessageBoardForm(request.POST)
        #走到这里说明验证符合要求了
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            print("="*50)
            print(title)
            print(content)
            print(email)
            print(reply)
            print("="*50)

            return HttpResponse("SUCCESS")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("FAIL")

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            telephone = forms.cleaned_data.get('telephone')
            email = forms.cleaned_data.get('email')
            User.objects.create(username=username,telephone=telephone,email=email)
            return HttpResponse("注册成功")
        else:
            print(forms.get_errors())
            return HttpResponse("注册失败")


