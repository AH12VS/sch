from django.urls import path, re_path
from .views import news_view, news_page_view

app_name = "news"

urlpatterns = [
    path("", news_view, name="news_page"),
    re_path(r"n/(?P<slug>[-\w]+)/", news_page_view, name="news_page_page"),
]
