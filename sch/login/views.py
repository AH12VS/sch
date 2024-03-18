from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home:home_page")

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            nat_code = cd["nat_code"]
            passwd = cd["passwd"]
            user = authenticate(request, nat_code=nat_code, password=passwd)
            if user != None and user.is_active:
                login(request, user)
                return redirect("home:home_page")
            else:
                form.add_error(None, "نام کاربری یا رمز عبور اشتباه میباشد")
                messages.error(request, "نام کاربری یا رمز عبور اشتباه میباشد")

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)

    return render(request, "login/login.html")
