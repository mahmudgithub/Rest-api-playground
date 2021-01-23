from django.db import models

class one(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class two(models.Model):
    board=models.CharField(max_length=10)
    roll=models.IntegerField()
    def __str__(self):
        return self.board

