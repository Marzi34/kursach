from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)

class Agent(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Client(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username