# Generated by Django 5.0.2 on 2024-03-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_articlemodel_time_for_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='slug_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان اسلاگ'),
        ),
    ]