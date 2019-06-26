from rest_framework import serializers

from .models import Book
class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ("url","b_name","b_price")

class Book1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id","b_name","b_price")