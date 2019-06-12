from django.http import HttpResponse
from django.shortcuts import reverse,redirect

# Create your views here.
def index(request):
    #http://127.0.0.1:8001/?username=kangbazi
    username = request.GET.get('username')
    if username:
        return HttpResponse("后台首页")
    else:
        # login_url = reverse('cms:login')
        # print("="*50)
        # print(login_url)
        # print("="*50)
        # return redirect(login_url)
        current_namespace = request.resolver_match.namespace
        print("="*50)
        print(current_namespace)
        print("="*50)
        return redirect(reverse("%s:login" % current_namespace))

def login(request):
    return HttpResponse("后台登录首页")