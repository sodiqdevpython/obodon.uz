from django.db import models

# Create your models here.
class Valantyorlar(models.Model):
    fio = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/')
    text = models.CharField(max_length=500)