from django.db import models
import os
from typing import Callable
from dataclasses import dataclass
import base64
import hashlib
import hmac

# Create your models here.
# Модель ссылки
class UrlShorter(models.Model):
    created = models.DateTimeField(auto_now_add=True)  # дата создания
    long_url = models.URLField()  # полная ссылка
    short_url = models.URLField(max_length=10, unique=True, blank=True)  # короткая ссылка
    clicks = models.PositiveIntegerField(default=0)  # сколько раз использовали ссылку


    class Meta:
        ordering = ["-clicks"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def clicked(self):
        self.clicks += 1
        self.save()

