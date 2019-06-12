from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

# Create your views here.

class Person(object):
    def __init__(self,username):
        self.username = username

def index(request):
    # html = render_to_string('index.html')
    # return HttpResponse(html)
    #p = Person('zhangliang')
    # context = {
    #     'person':p.username
    # }
    # return render(request, 'index.html',context={"username":"kangbazi"})
    # context = {
    #     'person':{
    #         'username':'zhangliang'
    #     }
    # }

    context = {
        'persons':(
            '苍老师',
            '上老师',
            "龙老师",
            "吉老师"
        )
    }
    return render(request, 'index.html',context=context)
