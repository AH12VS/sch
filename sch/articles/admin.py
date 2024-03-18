from django.contrib import admin
from .models import ArticleModel, ArticleCommentModel


@admin.register(ArticleModel)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "author", "status",
                    "created", "publish", "updated", "views_count", )
    list_editable = ("title", "status", )
    list_filter = ("title", "author", "status",
                   "created", "publish", "updated", )
    search_fields = ("title", "status", "author", )
    # prepopulated_fields = {"slug": ("title", "author", "slug_time", ), }


@admin.register(ArticleCommentModel)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ("article", "name", "created", "is_active",)
    list_editable = ("is_active", )
    list_filter = ("article", "created", "is_active", )
    search_fields = ("article", "name", )
