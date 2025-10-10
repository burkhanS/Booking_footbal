from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_owner = models.BooleanField(default=False)
    # is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username









