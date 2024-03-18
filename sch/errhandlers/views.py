from django.shortcuts import render

def err_404_view(request, exception):
    return render(request, "errhandlers/404.html")