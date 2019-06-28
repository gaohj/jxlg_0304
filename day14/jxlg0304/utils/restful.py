
# {
#     "message": "短信发送成功",
#     "data": {
#         "count": 1, /*发送数量*/
#         "fee": 1, /*扣除条数*/
#         "sid": "23d6bc4913614919a823271d820662af" /*短信ID*/
#     },
#     "code": 0 /*发送成功*/
# }
from django.http import JsonResponse
class HttpCode(object):
    ok = 200
    paramserror = 400
    unauth = 403
    methoderror = 405
    servererror = 500

def result(code=HttpCode.ok,message="",data=None,kwargs=None):
    json_dict = {"code":code,"message":message,"data":data}
    if kwargs and isinstance(kwargs,dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict)


def ok():
    return result()

def params_error(message="",data=None):
    return result(code=HttpCode.paramserror,message=message,data=data)

def unauth_error(message="",data=None):
    return result(code=HttpCode.unauth,message=message,data=data)

def method_error(message="",data=None):
    return result(code=HttpCode.methoderror,message=message,data=data)

def server_error(message="",data=None):
    return result(code=HttpCode.servererror,message=message,data=data)
