from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.http import require_POST
from .forms import LoginForm
from utils import restful
# Create your views here.
# def img_captcha(request):
#     text = 'kangbazi'
#     cache.set(text.lower(),text.lower(),5*60)
#     return HttpResponse("图形验证码")
@require_POST
def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request,username=telephone,password=password)
        if user:
            if user.is_active:
                login(request,user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return restful.ok()
            else:
                return restful.unauth_error(message="您的账户已经被冻结了")
        else:
            return restful.params_error(message="手机号或者密码错误")
    else:
        errors = form.get_errors()
        return restful.params_error(message=errors)