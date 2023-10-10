from django.shortcuts import render
from news.models import News
# Create your views here.


def asosiy_sahifa(request):
    data = News.objects.all()[::-1][:7]
    context = {
        'data': data
    }
    return render(request, 'index.html', context=context)
