from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    gitHub = models.URLField(max_length=50)
    userName = models.CharField(max_length=8)
    password = models.CharField(max_length=10)