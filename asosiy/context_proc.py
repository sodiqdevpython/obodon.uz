from news.models import Kategoriya, News

def category(request):
    viloyat = Kategoriya.objects.all()[:12]
    l_news = News.objects.all()[::-1][:6]
    context = {
        'viloyat':viloyat,
        'l_news':l_news,
    }
    return context