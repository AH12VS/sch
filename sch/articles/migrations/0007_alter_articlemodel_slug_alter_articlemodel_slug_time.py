# Generated by Django 5.0.2 on 2024-03-01 17:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_articlemodel_slug_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='slug_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان اسلاگ'),
        ),
    ]