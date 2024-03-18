from django.urls import path
from .views import staffs_view, staff_view

app_name = "users"

urlpatterns = [
    path("", staffs_view, name="staffs_page"),
    path("s/<pk>", staff_view, name="staff_page"),
]
