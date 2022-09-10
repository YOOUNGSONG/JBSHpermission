from django.db import models


# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=10)
    num = models.IntegerField()

    def __str__(self):
        return self.num, self.name
