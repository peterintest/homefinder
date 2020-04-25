from django.db import models
from django.utils import timezone

class Staff(models.Model):
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    start_date = models.DateTimeField(default=timezone.now, blank=True)
    
    class Meta: 
        verbose_name_plural = "staff"

    def __str__(self):
        return self.name
