from django.urls import path
from . import views
app_name = 'front'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('detail/<article_id>/<page>/',views.article_detail,name='detail'),

]