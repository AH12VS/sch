# Generated by Django 5.0.3 on 2024-03-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_articlemodel_views_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='views_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]