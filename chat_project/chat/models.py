from django.db import models

# Create your models here.
class ChatMessage(models.Model):
     content= models.CharField(max_length=1000)
     timeStamp = models.DateTimeField(auto_now=True)
     group=models.ForeignKey('Room_Name',on_delete=models.CASCADE)


class Room_Name(models.Model):
     room_name=models.CharField(max_length=200)
     created_at=models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.room_name
     
