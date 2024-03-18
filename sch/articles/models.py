from django.db import models
from django.urls import reverse
from users.models import UserModel
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from taggit.managers import TaggableManager

class ArticleModel(models.Model):
    STATUS_CHOICES = (
        ("draft", "پبش نویس"),
        ("published", "منتشر شده"),
    )
    title = models.CharField(verbose_name="عنوان", max_length=250)
    thumbnail = models.ImageField(verbose_name="عکس کاور", upload_to="img/articles/", blank=True, null=True)
    body_pre = models.CharField(verbose_name="متن پیش نمایش", max_length=250)
    body = RichTextUploadingField(verbose_name="محتوا")
    author = models.ForeignKey(UserModel, models.CASCADE, related_name="author_posts", verbose_name="نویسنده")
    status = models.CharField(verbose_name="وضعیت", max_length=15, choices=STATUS_CHOICES, default="draft")
    slug = models.SlugField(verbose_name="آدرس", unique=True, allow_unicode=True, blank=True, null=True)
    created = models.DateTimeField(verbose_name="زمان ساخت", auto_now_add=True)
    publish = models.DateTimeField(verbose_name="زمان انتشار", auto_now=True)
    updated = models.DateTimeField(verbose_name="زمان بروزرسانی", auto_now=True)
    slug_time = models.DateTimeField(verbose_name="زمان اسلاگ", default=timezone.now)
    views_count = models.PositiveSmallIntegerField(verbose_name="تعداد ویو ها", default=0, editable=False)
    tags = TaggableManager(verbose_name="برچسب ها")


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("articles:article_page", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True) + '-' + str(slugify(self.slug_time, allow_unicode=True)).replace("-", "")
        super(ArticleModel, self).save(*args, **kwargs)


class ArticleCommentModel(models.Model):
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, related_name="article_comments")
    name = models.CharField(max_length=60)
    comment_msg = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
