from django.db import models

# Create your models here.
class contactInfo(models.Model):
    name = models.CharField(max_length=50)