from django.db import models

# Create your models here.
class Book(models.Model):
    b_name = models.CharField(max_length=30)
    b_price = models.FloatField(default=10)

