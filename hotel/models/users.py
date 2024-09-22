from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.email