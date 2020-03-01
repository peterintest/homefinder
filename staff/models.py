from django.db import models

from datetime import datetime

class Staff(models.Model):
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    start_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
