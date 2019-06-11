from django.http import HttpResponse

def movie(request):
    return HttpResponse("这是电影首页")
