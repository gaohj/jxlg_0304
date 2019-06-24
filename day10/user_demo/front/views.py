from django.shortcuts import render,redirect,reverse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
# from .models import Person
from .models import User
from .forms import LoginForm


def index(request):
    #user = User.objects.create_user(username='lixi',email='lixi@outlook.com',password='123456')
    #user = User.objects.create_superuser(username='lushihao',email='shihao@outlook.com',password='123456')
    # user = User.objects.get(pk=3)
    # user.set_password('654321')
    # user.save()
    # username = 'lushihao'
    # password = '654321'
    # user = authenticate(request,username=username,password=password)
    # if user:
    #     print('%s用户验证成功' % user.username)
    # else:
    #     print('用户登录失败')
    # user = User.objects.create_user(username='lixi', email='lixi@outlook.com', password='123456')
    return render(request,'index.html')

# def proxy_view(request):
#
#     # Person.objects.all()
#     # User.objects.all()
#     blacklist = Person.get_blacklist()
#     for person in blacklist:
#         print(person.username)
#
#     return HttpResponse("获取黑名单成功")
def my_authenticate(telephone,password):
    user = User.objects.filter(extension__telephone=telephone).first()
    if user:
        is_correct = user.check_password(password)
        if is_correct:
            return user
        else:
            return None
    else:
        return None
def one_view(request):
    # user = User.objects.create_user(username='ziyi',email='zoyi@163.com',password='123456')
    # user.extension.telephone = '18888888888'
    # user.save()
    telephone = request.GET.get('telephone')
    password = request.GET.get('password')
    user = my_authenticate(telephone,password)
    if user:
        print("%s验证成功" % user.username)
    else:
        print("用户名或者密码错误")
    return HttpResponse("一对一扩展User模型")


def inherit_view(request):
    # telephone = '18888888888'
    # username = 'kangbazi'
    # password = '123456'
    # email = 'ziyi@gmail.com'
    # school = '江西理工大学'
    # user = User.objects.create_superuser(telephone=telephone,username=username,password=password,email=email,school=school)
    # user.save()
    # user = authenticate(request,username='18888888888',password='123456')
    # if user:
    #     print("%s验证成功" % user.username)
    # else:
    #     print("验证失败")
    # user = User.objects.create_superuser(telephone='18777777777', username='jiali', password='jingjing', email='jingjing@gmail.com')
    # user.save()
    # return HttpResponse("保持字段不变的情况下 添加两个字段")

    user = authenticate(request, username='18777777777', password='jingjing')
    if user:
        print("%s验证成功" % user.username)
    else:
        print("验证失败")
    return HttpResponse("把原有的user模型字段全部打乱该留的留该删除的删除")


def my_login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request,username=telephone,password=password)
            if user and user.is_active:
                login(request,user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return HttpResponse("登录成功")
            else:
                return HttpResponse("用户名或者密码失败")


        else:
            print(form.errors.get_json_data())
            return redirect(reverse('index'))
@login_required(login_url='/login/')
def profile(request):
    return HttpResponse("只有登录成功以后才可以查看到我")

def my_logout(request):
    logout(request)
    return redirect(reverse('index'))

