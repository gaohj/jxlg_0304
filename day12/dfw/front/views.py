from django.shortcuts import render
from .models import Book
# Create your views here.
from rest_framework import viewsets
from .serializers import BookSerializers,Book1Serializers

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Book1Serializers

