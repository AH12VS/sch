from django.urls import path, re_path
from .views import events_view, event_view

app_name = "events"

urlpatterns = [
    path("", events_view, name="events_page"),
    re_path(r"e/(?P<slug>[-\w]+)/", event_view, name="event_page"),
]
