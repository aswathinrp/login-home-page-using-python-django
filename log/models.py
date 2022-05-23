from email.mime import image
from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=255)
    image=models.CharField(max_length=2500)
    description=models.CharField(max_length=255)