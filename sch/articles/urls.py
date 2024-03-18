from django.urls import path, re_path
from .views import articles_view, article_view

app_name = "articles"

urlpatterns = [
    path("", articles_view, name="articles_page"),
    re_path(r"filterd/(?P<tag_slug>[-\w]+)/", articles_view, name="articles_tag_filtered_page"),
    re_path(r"a/(?P<slug>[-\w]+)/", article_view, name="article_page"),
]
