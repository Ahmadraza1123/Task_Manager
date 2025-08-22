from email.policy import default

from django.db import models


class Task(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Process', 'Process'),
        ('Completed', 'Completed'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    deccription = models.TextField(max_length=500)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)