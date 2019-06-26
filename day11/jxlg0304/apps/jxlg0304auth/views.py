from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.http import HttpResponse
# Create your views here.
def img_captcha(request):
    text = 'kangbazi'
    cache.set(text.lower(),text.lower(),5*60)
    return HttpResponse("图形验证码")

