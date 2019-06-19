"""classview_demo URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views as index_view
from article import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',index_view.index,name='index'),
    path('book_list/',index_view.BookListView.as_view(),name='book_list'),
    path('add_book/',index_view.AddBookView.as_view(),name='add_book'),
    path('detail/<book_id>/',index_view.BookDetailView.as_view(),name='detail'),
    path('list/',views.ArticleListView.as_view(),name="article_list"),
    # path('about/',TemplateView.as_view(template_name='about.html'),name="about"),
    path('about/',index_view.AboutView.as_view(),name='about')
]
