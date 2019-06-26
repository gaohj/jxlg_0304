from django.shortcuts import render
from .models import Book,Game,Movie
# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView
from .serializers import BookSerializers,Book1Serializers,GameSerializers,MovieSerializers


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Book1Serializers


class GameView(ListAPIView):
    #只允许你用来查看的  也就是 只允许get 请求
    queryset = Game.objects.all()
    serializer_class = GameSerializers

class Game1View(CreateAPIView):
    #只允许 post请求
    queryset = Game.objects.all()
    serializer_class = GameSerializers

class Game2View(ListCreateAPIView):
    #允许你get 和 post 请求
    queryset = Game.objects.all()
    serializer_class = GameSerializers


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers