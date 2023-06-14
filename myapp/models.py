from django.db import models

# Create your models here.
class CustomUser(models.Model):
    name=models.CharField(max_length=10)

# Create your models here.
class Chat(models.Model):
    message=models.CharField(max_length=256)
    def __str__(self) -> str:
        return self.message
    
# class ChatGroup(models.Model):
#     user1=models.CharField(max_length=100)
#     user2=models.CharField(max_length=100)
#     messages=models.ForeignKey(Chat,on_delete=models.CASCADE)

