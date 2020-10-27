from django.db import models

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    source = models.CharField(max_length=50)

class MaskHistory(models.Model):
    date = models.CharField(max_length=20, primary_key=True)
    outing = models.IntegerField()
    wearing = models.IntegerField()
