# Generated by Django 5.0.3 on 2024-03-11 19:30

import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_articlemodel_tags'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='برچسب ها'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='views_count',
            field=models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='تعداد ویو ها'),
        ),
    ]
