from rest_framework import routers
from django.urls import path
from django.conf.urls import url
from . import views
router = routers.DefaultRouter()
router.register(r'book',views.BookView)

urlpatterns = [
    path('game/',views.Game2View.as_view()),
    url(r'movie/$',views.MovieView.as_view(
        actions={
            "get":"list",
            "post":"create",
        }
    )),
   url(r'^movie/(?P<pk>\d+)/',views.MovieView.as_view(
        actions={
            "get":"retrieve",
            "put":"update",
            "delete":"destroy",
        }
    )),
]