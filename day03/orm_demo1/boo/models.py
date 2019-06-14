from django.db import models
from datetime import datetime
# # Create your models here.
# class Book(object):
#     username = 'asdf'
#     age = "adf"
class Book(models.Model):
    name = models.CharField(max_length=20,null=False)
    author = models.CharField(max_length=20,null=False)
    pub_time = models.DateTimeField(default=datetime.now)
    price = models.FloatField(default=0)

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,null=False)
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'articles'
        ordering = ['pub_time']
