from django.db import models

class MaskHistory(models.Model):
    date = models.CharField(max_length=20, primary_key=True)
    outing = models.IntegerField()
    wearing = models.IntegerField()
    withMask = models.BooleanField()
