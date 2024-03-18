# Generated by Django 5.0.2 on 2024-03-01 18:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsmodel',
            name='time_for_slug',
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='slug_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان اسلاگ'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='آدرس'),
        ),
    ]