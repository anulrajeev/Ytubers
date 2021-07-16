from django.contrib import messages
from django.db import models
from django.db.models.fields import CharField
from datetime import datetime
# Create your models here.

class Contacttuber(models.Model):
    name = models.CharField(max_length=255)
    phone= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    company_name= models.CharField(max_length=255)
    subject= models.TextField()
    message= models.TextField()
    created_date=models.DateTimeField(default =datetime.now, blank=True)