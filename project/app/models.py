from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    course = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)
    fees = models.IntegerField()
    