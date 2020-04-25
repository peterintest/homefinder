from django.db import models
from django.utils import timezone
from customers.models import Customer
from listings.models import Listing
from staff.models import Staff

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    listing = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True)
    agent = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    completion_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return str(self.listing)

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    listing = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True)
    agent = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    completion_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return str(self.listing)
