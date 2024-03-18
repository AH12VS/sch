from django.contrib import admin
from .models import NewsModel


@admin.register(NewsModel)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "author", "status",
                    "created", "publish", "updated", )
    list_editable = ("title", "status", )
    list_filter = ("title", "author", "status",
                   "created", "publish", "updated", )
    search_fields = ("title", "status", "author", )
    # prepopulated_fields = {"slug": ("title", "author", "time_for_slug", ), }
