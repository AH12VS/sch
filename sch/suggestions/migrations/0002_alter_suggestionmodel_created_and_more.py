# Generated by Django 5.0.3 on 2024-03-07 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestionmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال'),
        ),
        migrations.AlterField(
            model_name='suggestionmodel',
            name='stud_field',
            field=models.CharField(choices=[('computer', 'کامپیوتر'), ('chemical', 'شیمیایی')], default='computer', max_length=15, verbose_name='رشته ی تحصیلی'),
        ),
        migrations.AlterField(
            model_name='suggestionmodel',
            name='sug_msg',
            field=models.TextField(verbose_name='متن پیام'),
        ),
        migrations.AlterField(
            model_name='suggestionmodel',
            name='year',
            field=models.CharField(choices=[('y1', 'سال اول'), ('y2', 'سال دوم'), ('y3', 'سال سوم')], default='y1', max_length=5, verbose_name='پایه تحصیلی'),
        ),
    ]
