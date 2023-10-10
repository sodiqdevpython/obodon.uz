from django.urls import path
from .views import yangiliklar,detail
urlpatterns = [
    path('',yangiliklar, name='xabarlar'),
    path('article/<slug:slug>/', detail, name = 'detail')
]