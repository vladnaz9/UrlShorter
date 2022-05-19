from django.shortcuts import render
from django.http import HttpResponse
from .models import UrlShorter
from .forms import ShortUrlForm

# Create your views here.
# Главная страница
def index(request):
    if(request.method == 'POST'):
        form = ShortUrlForm(request.POST)
        short_url = form.save()
        data = {
            'short_url': short_url
        }
        return render(request, 'webapp/newUrl.html', data)
    form = ShortUrlForm()

    context = {'form': form}
    return render(request, 'webapp/index.html', context)


def getShortUrl(request):
    return


# достать все ссылки
def showAll(request):
    urls = UrlShorter.objects.all()

    allUrls = []
    for url in urls:
        view = {
            'str': url.__str__(),
            'clicks': url.clicks
        }

        allUrls.append(view)

    context = {'allUrls': allUrls}

    return render(request, 'webapp/allUrls.html', context)
