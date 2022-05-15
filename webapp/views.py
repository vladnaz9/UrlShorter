from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Главная страница
def index(request):
    return render(request, 'webapp/index.html')


