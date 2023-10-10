from django.db import models
from ckeditor.fields import RichTextField


class Kategoriya(models.Model):
    nomi = models.CharField(
        max_length=500, help_text="Viloyat nomini kiriting: ")

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = 'Viloyatlar'
        verbose_name_plural = 'Viloyatlar'
        ordering = ['nomi']


class News(models.Model):
    sarlavha = models.CharField(max_length=200, help_text='Yangilik sarlavhasi')
    slug = models.SlugField(max_length=200, help_text="Slug buni yozishingiz shart emas o'zi yozib beradi !")
    kategoriya = models.ForeignKey(Kategoriya, on_delete=models.CASCADE, help_text="Ushbu ma'lumot qaysi viloyatga tegishliligi")
    rasm = models.ImageField(upload_to='media/', help_text="Yangilik uchun kamida 1 ta rasm qo'yish shart")
    nashr_vaqti = models.DateTimeField(auto_now_add=True)
    matn = RichTextField(help_text="Yangilik matni")

    def __str__(self):
        return self.sarlavha

    class Meta:
        verbose_name = 'Yangiliklar'
        verbose_name_plural = 'Yangiliklar'
