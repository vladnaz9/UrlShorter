from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import UrlShorter
from .forms import ShortUrlForm


# Create your views here.
# Главная страница с выводом всех ссылок
def index(request):
    if request.method == 'POST':
        form = ShortUrlForm(request.POST)
        short_url = form.save()
        data = {
            'short_url': short_url
        }
        return render(request, 'webapp/newUrl.html', data)
    form = ShortUrlForm()

    context = {'form': form}
    return render(request, 'webapp/index.html', context)


# переход по короткой ссылке
def getShortUrl(request, param):
    url = UrlShorter.objects.filter(url_param=param).first()

    if url is None:
        return render(request, 'webapp/wrongUrl.html', context={'url': param})
    url.clicked()
    return redirect(url.long_url)


# достать все ссылки
def showAll(request):
    urls = UrlShorter.objects.all()
    if request.method == 'POST':
        delete(request, request.POST.get('id'))
    allUrls = []
    for url in urls:
        view = {
            'str': url.__str__(),
            'clicks': url.clicks,
            'id': url.id
        }

        allUrls.append(view)

    context = {'allUrls': allUrls}

    return render(request, 'webapp/allUrls.html', context)


# удаление урла по id
def delete(request, id):
    record = UrlShorter.objects.filter(id=id)

    if record is None:
        redirect(render(request, 'webapp/wrongUrl.html'))

    record.delete()
    return redirect('webapp .views.showAll')
