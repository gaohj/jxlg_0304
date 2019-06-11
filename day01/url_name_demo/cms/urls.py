from django.urls import path
from . import views
app_name = 'cms'
urlpatterns = [
    path('',views.index,name='index'),
    path('jiangxiligong/',views.login,name='login'),
]