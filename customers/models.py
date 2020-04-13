from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

