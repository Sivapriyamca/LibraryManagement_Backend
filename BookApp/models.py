from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    quantity = models.IntegerField()

