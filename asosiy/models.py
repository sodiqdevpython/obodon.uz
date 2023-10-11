from django.db import models

# Create your models here.
class Valantyorlar(models.Model):
    fio = models.CharField(max_length=250, verbose_name='Ism familiya')
    image = models.ImageField(upload_to='media/', verbose_name="Rasm qo'yish shart")
    text = models.CharField(max_length=500, verbose_name="Qisqacha ma'lumotlar")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Valantyorlar'
        verbose_name_plural = 'Valantyorlar'