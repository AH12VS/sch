from django.db import models

class SuggestionModel(models.Model):
    STUD_YEAR = (
        ("y1", "سال اول"),
        ("y2", "سال دوم"),
        ("y3", "سال سوم"),
    )
    STUD_FIELD = (
        ("computer", "کامپیوتر"),
        ("chemical", "شیمیایی"),
    )
    year = models.CharField(verbose_name="پایه تحصیلی", max_length=5, choices=STUD_YEAR, default="y1")
    stud_field = models.CharField(verbose_name="رشته ی تحصیلی", max_length=15, choices=STUD_FIELD, default="computer")
    sug_msg = models.TextField(verbose_name="متن پیام")
    created = models.DateTimeField(verbose_name="زمان ارسال", auto_now_add=True)

    def __str__(self):
        return self.sug_msg[0:100:1]


