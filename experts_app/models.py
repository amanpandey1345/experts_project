from django.db import models

# Create your models here.

class Regisration(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Number = models.IntegerField()
    Email = models.EmailField()
    Course = models.CharField(max_length=20)


class Enquiry(models.Model):
    Name = models.CharField(max_length=50)
    Number = models.IntegerField()
    City = models.CharField(max_length=50)
    Course = models.CharField(max_length=15)
