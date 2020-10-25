from django.db import models

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    source = models.CharField(max_length=50)