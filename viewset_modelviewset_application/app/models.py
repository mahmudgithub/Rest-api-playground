from django.db import models

class one(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    def __str__(self):
        return self.name 


class two(models.Model):
    age=models.IntegerField()
    roll=models.IntegerField()
