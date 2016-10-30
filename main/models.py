from django.db import models

# Create your models here.
class Algo(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField('created_at')
    updated_at = models.DateTimeField('updated_at')
    code = models.CharField(max_length=10000)