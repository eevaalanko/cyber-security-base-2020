from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nickname = models.TextField()

class Message(models.Model):
	sender =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_name')
	receiver = models.TextField()
	content = models.TextField()

