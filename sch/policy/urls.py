from django.urls import path
from .views import policy_view

app_name = "policy"
urlpatterns = [
    path("", policy_view, name="policy_page"),
]

