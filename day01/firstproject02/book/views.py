from django.http import HttpResponse

def book(request):
    return HttpResponse("这是图书首页")

def bookdetail(request):
    #http://127.0.0.1:8003/bookdetail/?id=3
    book_id = request.GET.get('id')
    return HttpResponse("您想要翻的牌子是:%s号" % book_id)

def details(request,book_id):
    response = "%s 书是好书,但是颜如玉在哪呢，" % book_id
    return HttpResponse(response)