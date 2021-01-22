from django.db import models

class one(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()

class two(models.Model):
    city=models.CharField(max_length=100)
    age=models.IntegerField()
