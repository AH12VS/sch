from django.contrib import admin
from .models import SuggestionModel

@admin.register(SuggestionModel)
class SuggestionModelAdmin(admin.ModelAdmin):
    ordering = ("-created",)
    list_display = ("__str__", "stud_field", "year", "created")
    list_filter = ("year", "stud_field", "created")
    search_fields = ("year", "stud_field", "created")


