from django.shortcuts import render
from news.models import News
from .models import Valantyorlar
# Create your views here.


def asosiy_sahifa(request):
    data = News.objects.all()[::-1][:7]
    context = {
        'data': data
    }
    return render(request, 'index.html', context=context)

def valantyorlar(request):
    data_obj = Valantyorlar.objects.all()

    context = {
        'data_obj':data_obj
    }
    return render(request, 'val.html', context=context)