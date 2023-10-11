from django.urls import path
from .views import asosiy_sahifa, valantyorlar
urlpatterns = [
    path('', asosiy_sahifa, name='asosiy'),
    path('valantyorlar/', valantyorlar, name='val')
]
