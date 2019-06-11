"""firstproject02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
#from django.http import HttpResponse #用来将内容返回给浏览器
#参数为字符串
# from book import views as book_view
from movie import views as movie_view
from shop import views as shop_view

# def index(request):
#     #request这个参数必须写  因为它包含我们前端所有的请求
#     return HttpResponse("这是首页")

urlpatterns = [
    # path('index/',index),#http://127.0.0.1:80001
    path('book/',include('book.urls')), #主url文件导入 模块图书的url
    path('movie/',movie_view.movie),
    path('shop/',shop_view.shop),
]
