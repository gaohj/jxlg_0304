from django.http import HttpResponse
from django.shortcuts import reverse,redirect

# Create your views here.
def index(request):
    #http://127.0.0.1:8001/?username=kangbazi
    username = request.GET.get('username')
    if username:
        return HttpResponse("前台首页")
    else:
        # login_url = reverse('front:login')
        # print("="*50)
        # print(login_url)
        # print("="*50)
        # return redirect(login_url)
        # detail_url = reverse('front:detail',kwargs={"article_id":1,"page":2})
        # return redirect(detail_url)
        login_url = reverse('front:login')+"?next=/"
        return redirect(login_url)
def login(request):
    return HttpResponse("前台登录首页")


def article_detail(request,article_id,page):
    text = "您想要查看的文章是:%s,位于 %s 一页" % (article_id,page)
    return HttpResponse(text)

