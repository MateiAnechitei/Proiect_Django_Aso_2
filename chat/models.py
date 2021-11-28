from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    message = models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey('Chatroom', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)


class Chatroom(models.Model):
    name = models.CharField(max_length=255)

