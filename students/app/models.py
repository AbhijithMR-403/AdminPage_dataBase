from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40, default='unknown@example.com')
    password=models.CharField(null=True)