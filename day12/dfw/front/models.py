from django.db import models

# Create your models here.
class Book(models.Model):
    b_name = models.CharField(max_length=30)
    b_price = models.FloatField(default=10)


class Game(models.Model):
    g_name = models.CharField(max_length=30)
    g_price = models.FloatField(default=10)

class Movie(models.Model):
    m_name = models.CharField(max_length=30)
    m_price = models.FloatField(default=10)

