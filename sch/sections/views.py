from django.shortcuts import render


def computer_section_view(request):
    return render(request, "sections/section.html")
