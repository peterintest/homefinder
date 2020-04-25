from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from staff.models import Staff


class Listing(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    livingrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=timezone.now, blank=True)
 
    def __str__(self):
        return self.title

class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    keywords = models.CharField(max_length=200, blank=True)
    bedrooms = models.IntegerField(blank=True)
    max_price = models.IntegerField(blank=True)
    search_date = models.DateTimeField(default=timezone.now, blank=True)

    class Meta: 
        verbose_name_plural = "searches"
