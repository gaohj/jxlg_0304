from django.http import HttpResponse
from django.shortcuts import redirect,reverse

# Create your views here.
def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("后台首页")
    else:
        # return redirect('/signup/')
        # print(reverse('login'))
        return redirect(reverse('cms:login'))


def login(request):
    return HttpResponse("后台登录页")
