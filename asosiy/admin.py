from django.contrib import admin
from .models import Valantyorlar
# Register your models here.
@admin.register(Valantyorlar)
class AdminVal(admin.ModelAdmin):
    search_fields = ['fio']