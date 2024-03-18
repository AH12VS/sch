# Generated by Django 5.0.2 on 2024-02-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usermodel_img_prof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='edu',
            field=models.CharField(choices=[('sycle', 'سیکل'), ('diploma', 'دیپلم'), ('ass_deg', 'کاردانی'), ('bac_deg', 'لیسانس'), ('master', 'فوق لیسانس'), ('dr', 'دکترا')], default='sycle', max_length=15, verbose_name='تحصیلات'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='pos',
            field=models.CharField(choices=[('manager', 'مدیر'), ('assistant', 'معاون اجرایی'), ('supervisor', 'سرپرست بخش')], default='supervisor', max_length=15, verbose_name='منصب'),
        ),
    ]