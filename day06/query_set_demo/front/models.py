from django.db import models


class Author(models.Model):
    """作者模型"""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'author'


class Publisher(models.Model):
    """出版社模型"""
    name = models.CharField(max_length=300)

    class Meta:
        db_table = 'publisher'


class Book(models.Model):
    """图书模型"""
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.FloatField()
    rating = models.FloatField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book'


class BookOrder(models.Model):
    """图书订单模型"""
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    price = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table = 'book_order'