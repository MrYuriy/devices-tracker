from django.conf import settings
from django.db import models
from device.models import Device

from user.models import User


# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    datetime = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

    class Meta:
        ordering = ["datetime"]

    def __str__(self):
        return f"User: {self.user}, datetime: {self.datetime}"
