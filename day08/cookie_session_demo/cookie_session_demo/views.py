from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware


def index(request):
    response = HttpResponse("Index")
    expires = datetime(year=2019,month=6,day=22,hour=20,minute=30,second=40)
    expires = make_aware(expires)
    response.set_cookie('user_id','xcxk',expires=expires,max_age=180,path='/cms/')
    return response

def delete_cookie(request):
    response = HttpResponse('delete')
    response.delete_cookie('user_id')
    return response

def cms_view(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)

def my_view(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)

def session_view(request):
    request.session['username'] = 'xxcxk'
    request.session['user_id'] = '444'
    # username = request.session.pop('username') #从session移除指定的字段
    # print(username) #打印的是移除的哪个值
    # request.session.clear() #删除当前用户的cookie
    # #request.session.flush() #注销登录常用这个 删除浏览器的session_id
    # print(request.session.get('username')) #查看移除以后session中的指定的值
    # request.session.set_expiry(None) #表示两周
    #request.session.set_expiry(-1) #表示永不过期
    request.session.set_expiry(0) #表示永不过期
    #request.session.clear_expired() #清空过期的session
    return HttpResponse("SESSION")
