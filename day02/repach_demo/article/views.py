from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("文章首页")

def article_list(request,year):
    text = "您输入的年份是:%s" % year
    return HttpResponse(text)

def article_list_month(request,month):
    text = "您输入的月份是:%s" % month
    return HttpResponse(text)

