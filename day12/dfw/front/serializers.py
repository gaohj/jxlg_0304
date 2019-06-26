from rest_framework import serializers

from .models import Book,Game,Movie
class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ("url","b_name","b_price")

class Book1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id","b_name","b_price")

class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ("id","g_name","g_price")

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id","m_name","m_price")