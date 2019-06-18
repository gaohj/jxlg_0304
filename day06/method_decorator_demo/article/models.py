from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table = 'article'
