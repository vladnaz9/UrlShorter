from django.db import models
import os
from typing import Callable
from dataclasses import dataclass
import base64
import hashlib
import hmac

# Модель ссылки
class UrlShorter(models.Model):
    created = models.DateTimeField(auto_now_add=True)  # дата создания
    long_url = models.URLField()  # полная ссылка
    short_url = models.URLField(unique=True, blank=True)  # короткая ссылка
    clicks = models.PositiveIntegerField(default=0)  # сколько раз использовали ссылку
    url_hash = models.CharField(max_length= 20) # храним url + соль

    class Meta:
        ordering = ["-clicks"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def clicked(self):
        self.clicks += 1
        self.save()

    def gen_hash_for_short_url(self, long_url) -> None:
        salt = os.urandom(32)
        hash = hashlib.pbkdf2_hmac('sha256', long_url.encode('utf-8'), salt, 100000)
        self.short_url = "".join(['http://127.0.0.1:8000/shorter/', hash])
        self.url_hash = f"${salt}${hash}"

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)