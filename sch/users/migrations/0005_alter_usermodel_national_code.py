# Generated by Django 5.0.2 on 2024-02-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_usermodel_national_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='national_code',
            field=models.CharField(max_length=10, unique=True, verbose_name='کد ملی'),
        ),
    ]
