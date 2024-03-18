from django.urls import path
from .views import contactus_view

app_name = "contactus"

urlpatterns = [
    path("", contactus_view, name="contactus_page"),
]
