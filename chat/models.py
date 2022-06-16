from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
class Room(models.Model):
    name = models.CharField(max_length=1000)
    # username = 
    
    def __str__(self):
        return self.name

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    def __str__(self):
        return self.room