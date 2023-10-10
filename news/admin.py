from django.contrib import admin
from .models import Kategoriya, News
# Register your models here.
admin.site.register(Kategoriya)

@admin.register(News)
class YangilikAdmin(admin.ModelAdmin):
    list_display = ['sarlavha', 'kategoriya','nashr_vaqti']
    prepopulated_fields = {"slug": ('sarlavha',)}
    list_filter = ['kategoriya','nashr_vaqti']
    search_fields = ['sarlavha', 'matn']