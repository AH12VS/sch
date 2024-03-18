from django.shortcuts import render, redirect
from .models import SuggestionModel
from .forms import SuggestionForm
from django.contrib import messages


def suggestion_view(request):
    form = SuggestionForm()
    if request.method == "POST":
        form = SuggestionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            year = cd["year"]
            stud_field = cd["stud_field"]
            sug_msg = cd["sug_msg"]

            sug_obj = SuggestionModel()
            sug_obj.year = year
            sug_obj.stud_field = stud_field
            sug_obj.sug_msg = sug_msg

            sug_obj.save()
            return redirect("home:home_page")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            
    return render(request, "suggestions/suggestion.html")
