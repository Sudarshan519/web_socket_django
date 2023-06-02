from django.db import models

# Create your models here.
class CustomUser(models.Model):
    name=models.CharField(max_length=10)