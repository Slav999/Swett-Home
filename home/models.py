from django.db import models


class Users(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
