from django.shortcuts import render

def contactus_view(request):
    return render(request, "contactus/contactus.html")
