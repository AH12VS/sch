# Generated by Django 5.0.2 on 2024-03-01 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_articlemodel_time_for_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlemodel',
            name='time_for_slug',
        ),
    ]
