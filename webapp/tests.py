from datetime import datetime

from django.test import TestCase
from django.db import models

# Create your tests here.
from webapp.models import UrlShorter


class ShortUrlTest(TestCase):
    def setUpTestData(cls):
        cls.url = UrlShorter.objects.create(
            long_url='https://github.com/',
            short_url='http://127.0.0.1:8000/shorter/919df7c1',
            url_param='919df7c1'
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.url.long_url, str)
        self.assertIsInstance(self.url.short_url, str)
        self.assertIsInstance(self.url.url_param, str)
        self.assertIsInstance(self.url.created, datetime)
        self.assertIsInstance(self.url.clicks, int)


    def test_string_working(self):
        url_str = f' {self.url.long_url} to {self.url.short_url}'
        self.assertEquals(str(self.url), url_str)

    def test_is_clicked(self):
        clicks = self.url.clicks
        self.url.clicked()
        self.assertEquals(clicks + 1, self.url.clicks)

