from django.db import models

# Create your models here.

class Scan(models.Model):
    scan_name = models.CharField(max_length=25,unique=True,verbose_name='Scan Name') 