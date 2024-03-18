from django.contrib import admin
from users.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    ordering = ("-date_joined",)
    list_display = ("nat_code", "email", "fname",
                    "lname", "pos", "date_joined", "is_active", "updated", "last_login")
    list_editable = ("pos", "is_active",)
    list_filter = ("date_joined", "pos", "last_login",
                   "is_active", "is_staff", "is_admin", "is_superuser")
    search_fields = ("nat_code", "email",
                     "fname", "lname", "pos", "date_joined")
