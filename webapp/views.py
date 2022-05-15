from django.shortcuts import render
from django.http import HttpResponse
from .models import UrlShorter

# Create your views here.
# Главная страница
def index(request):
    return render(request, 'webapp/index.html')


def getShortUrl(request):
    return


# достать все ссылки
def AllShorters(request):
    urls = UrlShorter.objects.all()

    allUrls = []
    for url in urls:
        view = {
            'str': url.__str__(),
            'clicks': url.clicks
        }

        allUrls.append(view)

    context: {'urls': allUrls}

    return render(request, 'webapp/allUrls.html', allUrls)
