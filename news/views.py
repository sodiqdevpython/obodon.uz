from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import News, Kategoriya
# Create your views here.

def yangiliklar(request):
    kategoriya = Kategoriya.objects.all()[:15]
    xabarlar = News.objects.all()[:6]
    xabarlar_yangi = News.objects.all()[::-1][:6]
    context = {
        'kategoriya':kategoriya,
        'xabarlar':xabarlar,
        'xabarlar_yangi':xabarlar_yangi,
    }
    return render(request, 'blog.html', context=context)

def detail(request, slug):
	data_detail = get_object_or_404(News, slug = slug)
	context = {
		'data_detail': data_detail
	}
	return render(request, 'detail.html', context = context)