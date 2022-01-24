import email
from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    specialization = models.CharField(max_length=50)
    phone = models.IntegerField()


