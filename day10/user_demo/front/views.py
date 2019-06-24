from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
# Create your views here.
from .models import Person

def index(request):
    #user = User.objects.create_user(username='lixi',email='lixi@outlook.com',password='123456')
    #user = User.objects.create_superuser(username='lushihao',email='shihao@outlook.com',password='123456')
    # user = User.objects.get(pk=3)
    # user.set_password('654321')
    # user.save()
    username = 'lushihao'
    password = '654321'
    user = authenticate(request,username=username,password=password)
    if user:
        print('%s用户验证成功' % user.username)
    else:
        print('用户登录失败')
    user = User.objects.create_user(username='lixi', email='lixi@outlook.com', password='123456')
    return HttpResponse("创建超级用户成功")

def proxy_view(request):
    blacklist = Person.get_blacklist()
    for person in blacklist:
        print(person.username)

    return HttpResponse("获取黑名单成功")
