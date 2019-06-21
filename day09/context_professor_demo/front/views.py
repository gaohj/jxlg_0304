from django.shortcuts import render,redirect,reverse
from .models import User
from django.views.generic import View
from .forms import SignUpForm,SignInForm
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def index(request):
    # users = User.objects.all()
    # for user in users:
    #     print(user)
    return render(request,'index.html')

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('register'))

class SignInView(View):
    def get(self,request):
        return render(request,'signin.html')
    def post(self,request):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username,password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                messages.info(request,'用户名或者密码错误')
                return redirect(reverse('signin'))
        else:
            # errors = form.errors.get_json_data()
            # print(errors)
            # print(form.get_errors())['用户名至少是6位', '密码至少是6位']
            errors = form.get_errors()
            for error in errors:
                messages.info(request,error)
            return redirect(reverse('signin'))

def blog(request):
    return render(request,'blog.html')

def video(request):
    return render(request,'video.html')

def logout(request):
    request.session.flush()
    return redirect(reverse('index'))
