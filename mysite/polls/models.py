from django.db import models
class Chp(models.Model):
    cid=models.IntegerField(primary_key=True)
    value=models.CharField(max_length=100)
class Pic(models.Model):
    pid=models.IntegerField(primary_key=True)
    value=models.CharField(max_length=100)
# Create your models here.
