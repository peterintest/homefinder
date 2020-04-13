from django.db import models
from datetime import datetime
from customers.models import Customer
from listings.models import Listing
from staff.models import Staff

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    agent = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    completion_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.listing

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    agent = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    completion_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.listing