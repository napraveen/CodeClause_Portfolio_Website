from django.db import models
from datetime import datetime

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=30)
    grade = models.CharField(max_length=100)

class Person(models.Model):
    username = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    skill1 =models.CharField(max_length=100, blank=True)
    skill2 = models.CharField(max_length=100, blank=True)
    skill3 =models.CharField(max_length=100, blank=True)
    post = models.CharField(max_length=100, blank=True)
    we1 = models.CharField(max_length=100, blank=True)
    we2 =models.CharField(max_length=100, blank=True)
    we3 = models.CharField(max_length=100, blank=True)
    des1 = models.CharField(max_length=120, blank=True)
    des2 =models.CharField(max_length=120, blank=True)
    des3=models.CharField(max_length=120, blank=True)
    eq= models.CharField(max_length=100, blank=True)
    selfdesc= models.CharField(max_length=1000, blank=True)

class Qrcode(models.Model):
    qrs = models.CharField(max_length=100, default=None)
