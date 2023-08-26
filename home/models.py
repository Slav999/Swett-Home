from django.db import models
from django.utils import timezone


class Users(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
