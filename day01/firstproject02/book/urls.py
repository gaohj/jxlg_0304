from django.urls import path   #所有关于图书的url全部写到这里
from . import views
urlpatterns = [
    path('', views.book),
    path('bookdetail/', views.bookdetail),
    # path('detail/<int:book_id>/',views.details),
    # path('detail/<str:book_id>/',views.details),
    # path('detail/<path:book_id>/',views.details),
    path('detail/<uuid:book_id>/', views.details),
]