from django.db import models

class PhoneNumber(models.Model):
    number = models.CharField(max_length=20, unique=True)
