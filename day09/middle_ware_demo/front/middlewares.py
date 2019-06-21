from .models import User
#get_response 是一个方法
def front_user_middlerware(get_response):
    print("在这个位置我们一般是用来初始化一些代码")
    def middleware(request):
        #执行的是request到达view之前执行的代码
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
        response = get_response(request) #以这个为界限
        #这个之前是request到达view之前
        #这个之后是 reponse 对象到达浏览器
        return response

    return middleware

