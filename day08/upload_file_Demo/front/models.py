from django.db import models
from django.core import validators
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # thumbnail = models.FileField(upload_to='%Y/%m/%d',validators=[validators.FileExtensionValidator(['txt'],message="缩略图必须为txt类型的文件")])
    #thumbnail = models.ImageField(upload_to='%Y/%m/%d')
    thumbnail = models.ImageField(upload_to='kangbazi')

