from django.db import models

# Create your models here.
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)


class ChatMessage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)