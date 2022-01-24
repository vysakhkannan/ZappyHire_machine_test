from django.db import models
import uuid


# Create your models here.

class Patients(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.IntegerField()



