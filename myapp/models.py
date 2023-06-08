from django.db import models

# Create your models here.
class CustomUser(models.Model):
    name=models.CharField(max_length=10)


# Create your models here.
class Chat(models.Model):
    message=models.CharField(max_length=256)