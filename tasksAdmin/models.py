from django.db import models

class Task(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    status_task = models.CharField(max_length=50,  blank=True)
    update_date_task = models.DateField(null=True, blank=True)
