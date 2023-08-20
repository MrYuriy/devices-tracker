from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from device.models import DeviceSite


# Create your models here.
class User(AbstractUser):
    site = models.ManyToManyField(DeviceSite, related_name="user")
    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username
    
    def get_absolute_url(self): # new
        return reverse("user:user-list")