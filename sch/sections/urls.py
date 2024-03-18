from django.urls import path
from .views import computer_section_view

app_name = "sections"

urlpatterns = [
    path("", computer_section_view, name="computer_section_page"),
]
