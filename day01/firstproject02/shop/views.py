from django.http import HttpResponse

def shop(request):
    return HttpResponse("这是商城首页")