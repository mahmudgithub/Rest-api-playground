from django.db import models

class one(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
