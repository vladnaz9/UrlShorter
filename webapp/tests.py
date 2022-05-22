from datetime import datetime
from django.test import TestCase
from django.db import models
from django.test.client import RequestFactory
from webapp.models import UrlShorter
from webapp.views import delete, getShortUrl, index, showAll


class ShortUrlTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = UrlShorter.objects.create(
            long_url='https://github.com/',
            short_url='http://127.0.0.1:8000/shorter/919df7c1',
            url_param='919df7c1'
        )
        cls.factory = RequestFactory()

    # проверка, что все поля создались правильно
    def test_it_has_information_fields(self):
        self.assertIsInstance(self.url.long_url, str)
        self.assertIsInstance(self.url.short_url, str)
        self.assertIsInstance(self.url.url_param, str)
        self.assertIsInstance(self.url.created, datetime)
        self.assertIsInstance(self.url.clicks, int)

    # проверка toString метода
    def test_string_working(self):
        url_str = f' {self.url.long_url} to {self.url.short_url}'
        self.assertEquals(str(self.url), url_str)

    # проверка увеличения кликов
    def test_is_clicked(self):
        clicks = self.url.clicks
        self.url.clicked()
        self.assertEquals(clicks + 1, self.url.clicks)

    # удаление объекта урла
    def test_it_can_delete(self):
        request = self.factory.get('/showAll/')
        delete(request, self.url.id)

    def test_getShorUrl_method(self):
        self.assertRedirects(getShortUrl(self.factory.get('/showAll/'), self.url.url_param), self.url.long_url,
                             fetch_redirect_response=False)

    def test_index_page(self):
        request = self.factory.get('')
        response = index(request)
        self.assertEquals(response.status_code, 200)


    def test_showAll_page(self):
        request = self.factory.get('/showALl/')
        response = showAll(request)
        self.assertEquals(response.status_code, 200)
