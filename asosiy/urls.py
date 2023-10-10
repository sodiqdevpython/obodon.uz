from django.urls import path
from .views import asosiy_sahifa
urlpatterns = [
    path('', asosiy_sahifa, name='asosiy')
]
