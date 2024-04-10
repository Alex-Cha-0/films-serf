from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    darkmode = models.BooleanField(
        'Темный режим',
        blank=True,
    )

    def __str__(self):
        return f"{self.user.username}, darkmode: {self.darkmode}"
