from django.db import models


# Create your models here.
class Saleservice(models.Model):
    title = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    image = models.CharField(max_length=400)
    provider = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)







