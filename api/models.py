from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    deccription = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)