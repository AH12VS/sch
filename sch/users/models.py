from django.db import models
# use to make an custom User Model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserModelManager(BaseUserManager):
    def create_user(self, nat_code, password, email="", fname="", lname="", age=1, edu="", pos=""):
        # check email if its empty or not
        if not email:
            raise ValueError("Email is Required")
        #
        # check nat_code
        if not nat_code:
            raise ValueError("National Code is Required")
        #
        user = self.model(nat_code=nat_code, email=self.normalize_email(email),
                          fname=fname, lname=lname, age=age, edu=edu, pos=pos)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nat_code, password, email="", fname="", lname="", age=1, edu="", pos=""):
        user = self.create_user(nat_code,
                                email, password, fname=fname, lname=lname, age=age, edu=edu, pos=pos)
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    EDU_CHOICES = (
        ("sycle", "سیکل"),
        ("diploma", "دیپلم"),
        ("ass_deg", "کاردانی"),
        ("bac_deg", "لیسانس"),
        ("master", "فوق لیسانس"),
        ("dr", "دکترا"),
    )
    POS_CHOICES = (
        ("manager", "مدیر"),
        ("assistant", "معاون اجرایی"),
        ("supervisor", "سرپرست بخش"),
    )

    # extras field
    nat_code = models.CharField(
        verbose_name="کد ملی", max_length=10, unique=True)
    email = models.EmailField(verbose_name="ایمیل",
                              max_length=250, unique=True)
    fname = models.CharField(verbose_name="نام", max_length=30)
    lname = models.CharField(verbose_name="نام خانوادگی", max_length=30)
    age = models.PositiveSmallIntegerField(verbose_name="سن")
    edu = models.CharField(verbose_name="تحصیلات",
                           max_length=15, choices=EDU_CHOICES, default="sycle")
    pos = models.CharField(verbose_name="منصب", max_length=15,
                           choices=POS_CHOICES, default="supervisor")
    img_prof = models.ImageField(
        verbose_name="عکس", upload_to="img/users/", blank=True, null=True)
    # end extras field

    # default django user fields
    date_joined = models.DateTimeField(
        verbose_name="زمان پیوستن", auto_now_add=True, unique=True)
    last_login = models.DateTimeField(verbose_name="آخرین ورود", auto_now=True)
    updated = models.DateTimeField(verbose_name="بروزرسانی", auto_now=True)
    #
    is_admin = models.BooleanField(verbose_name="مدیر", default=False)
    is_active = models.BooleanField(verbose_name="فعال", default=False)
    is_staff = models.BooleanField(verbose_name="کارمند", default=False)
    is_superuser = models.BooleanField(verbose_name="سوپریوزر", default=False)
    # end default django user fields

    # check for signup
    is_in_signup = models.BooleanField(
        verbose_name="در مرحله ی ثبت", default=True)
    passwd = models.CharField(
        verbose_name="رمز", max_length=200, null=True, blank=True)
    # end check for signup

    # token
    tmp_token = models.CharField(
        verbose_name="توکن موقت", max_length=10, null=True, blank=True)
    tmp_token_time = models.DateTimeField(
        verbose_name="زمان توکن موقت", null=True, blank=True)
    # end token

    # object manger
    objects = UserModelManager()
    # object manger

    # USERNAME_FIELD = "email"  # use email for username
    USERNAME_FIELD = "nat_code"  # use nat_code for username

    # show first part of email (-> before @)
    def __str__(self):
        return (self.fname + ' ' + self.lname)
        # return str(self.email).split("@")[0]
    #

    # default django user method
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    # end default django user method

    def get_absolute_url(self):
        return reverse("users:staff_page", args=[self.id])
