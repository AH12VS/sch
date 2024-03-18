from django.urls import path
from .views import suggestion_view

app_name = "suggestions"

urlpatterns = [
    path("", suggestion_view, name="suggestion_page"),
]

