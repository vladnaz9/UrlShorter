# Generated by Django 4.0.4 on 2022-05-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlshorter',
            name='url_hash',
        ),
        migrations.AddField(
            model_name='urlshorter',
            name='url_param',
            field=models.CharField(blank=True, default='0', max_length=20),
        ),
    ]