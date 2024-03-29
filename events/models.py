from django.db import models
from django.utils import timezone
from staff.models import Staff

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, blank=True)
    organiser = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)    

    def __str__(self):
        return self.title
