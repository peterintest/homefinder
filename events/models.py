from django.db import models
from datetime import datetime
from staff.models import Staff

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    organiser = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)    

    def __str__(self):
        return self.title
