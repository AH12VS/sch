# Generated by Django 5.0.3 on 2024-03-11 19:40

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_eventmodel_time_for_slug_eventmodel_slug_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوا'),
        ),
    ]
